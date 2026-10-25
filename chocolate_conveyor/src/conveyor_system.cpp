#include <iostream>
#include <gz/sim/System.hh>
#include <gz/sim/Model.hh>
#include <gz/sim/Link.hh>
#include <gz/sim/Util.hh>
#include <gz/sim/components/Model.hh>
#include <gz/sim/components/Name.hh>
#include <gz/sim/components/Pose.hh>
#include <gz/plugin/Register.hh>

#include <algorithm>
#include <cmath>
#include <string>

namespace chocolate_conveyor
{
class ConveyorSystem :
  public gz::sim::System,
  public gz::sim::ISystemPreUpdate
{
public:
  void PreUpdate(
    const gz::sim::UpdateInfo &_info,
    gz::sim::EntityComponentManager &_ecm) override
  {
    if (_info.paused)
      return;

    constexpr double beltX = 1.0;
    constexpr double beltY = -2.0;
    constexpr double beltZ = 0.75;
    constexpr double beltLength = 4.90;
    constexpr double beltWidth = 0.38;
    constexpr double targetSpeed = 0.3;
    constexpr double gain = 120.0;
    constexpr double maxForce = 15.0;

    _ecm.Each<
      gz::sim::components::Model,
      gz::sim::components::Name,
      gz::sim::components::Pose>(
      [&](const gz::sim::Entity &_entity,
          const gz::sim::components::Model *,
          const gz::sim::components::Name *_name,
          const gz::sim::components::Pose *_pose) -> bool
      {
        if (_name->Data().find("chocolate_bar") == std::string::npos)
          return true;

        const auto &pos = _pose->Data().Pos();

        // Slett sjokolader når de når enden av samlebåndet.
        if (std::abs(pos.X() - beltX) <= beltWidth / 2.0 &&
            pos.Z() >= beltZ &&
            pos.Z() <= beltZ + 0.20 &&
            pos.Y() >= 0.35)
        {
          _ecm.RequestRemoveEntity(_entity);
          return true;
        }

        // Slett sjokoladeplater som har falt av transportbåndet.
        if (pos.Z() < 0.30)
        {
          _ecm.RequestRemoveEntity(_entity);
          return true;
        }

        // Bare plater som ligger på høyre samlebånd.
        if (std::abs(pos.X() - beltX) > beltWidth / 2.0 ||
            (pos.Y() - beltY) > beltLength / 2.0 ||
            (pos.Y() - beltY) < -beltLength / 2.0 ||
            pos.Z() < beltZ ||
            pos.Z() > beltZ + 0.20)
          return true;

        static bool reported = false;

        if (!reported)
        {
          std::cout << "[CONVEYOR] Chocolate detected: "
                    << _name->Data()
                    << " at " << pos << std::endl;
          reported = true;
        }

        gz::sim::Model model(_entity);
        gz::sim::Link link(model.CanonicalLink(_ecm));

        if (!link.Valid(_ecm))
          return true;

        // Hastighetsmåling må aktiveres i Gazebo.
        link.EnableVelocityChecks(_ecm);

        const auto velocity = link.WorldLinearVelocity(_ecm);

        if (_info.iterations % 1000 == 0)
        {
          std::cout << "[CONVEYOR] Velocity available: "
                    << (velocity.has_value() ? "YES" : "NO");
          if (velocity)
            std::cout << " | Y = " << velocity->Y();
          std::cout << std::endl;
        }

        if (!velocity)
          return true;

        // Proporsjonal hastighetsregulator.
        const double error = targetSpeed - velocity->Y();
        const double force = std::clamp(
          gain * error, -maxForce, maxForce);

        // Påfør kraft langs båndet, uten å overstyre gravitasjonen.
        link.AddWorldForce(
          _ecm, gz::math::Vector3d(0, force, 0));

        return true;
      });
  }
};
}

GZ_ADD_PLUGIN(
  chocolate_conveyor::ConveyorSystem,
  gz::sim::System,
  chocolate_conveyor::ConveyorSystem::ISystemPreUpdate
)
