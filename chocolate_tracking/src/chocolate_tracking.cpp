#include <rclcpp/rclcpp.hpp>
#include <chocolate_interfaces/msg/chocolate_pose.hpp>
#include <chocolate_interfaces/msg/chocolate_pose_array.hpp>

#include <gz/transport/Node.hh>
#include <gz/msgs/pose_v.pb.h>

#include <chrono>
#include <functional>
#include <memory>
#include <string>

class ChocolateTracking : public rclcpp::Node
{
public:
    ChocolateTracking() : Node("chocolate_tracking")
    {
        publisher_ =
            this->create_publisher<chocolate_interfaces::msg::ChocolatePoseArray>(
                "/chocolate/poses", 10);

        bool subscribed = gz_node_.Subscribe(
            "/world/chocolate_factory/dynamic_pose/info",
            &ChocolateTracking::OnPoses,
            this);

        if (!subscribed)
        {
            RCLCPP_ERROR(this->get_logger(), "Failed to subscribe to Gazebo");
        }
        else
        {
            RCLCPP_INFO(this->get_logger(), "Chocolate tracking started");
            RCLCPP_INFO(this->get_logger(), "Publishing on /chocolate/poses");
        }
    }

private:
    void OnPoses(const gz::msgs::Pose_V &_msg)
    {
        chocolate_interfaces::msg::ChocolatePoseArray array;

        array.header.stamp = this->now();
        array.header.frame_id = "world";

        for (int i = 0; i < _msg.pose_size(); ++i)
        {
            const auto &pose = _msg.pose(i);

            if (pose.name().rfind("chocolate_bar_", 0) != 0)
                continue;

            chocolate_interfaces::msg::ChocolatePose chocolate;

            chocolate.name = pose.name();
            chocolate.id = pose.id();

            chocolate.pose.position.x = pose.position().x();
            chocolate.pose.position.y = pose.position().y();
            chocolate.pose.position.z = pose.position().z();

            chocolate.pose.orientation.x = pose.orientation().x();
            chocolate.pose.orientation.y = pose.orientation().y();
            chocolate.pose.orientation.z = pose.orientation().z();
            chocolate.pose.orientation.w = pose.orientation().w();

            array.chocolates.push_back(chocolate);
        }

        publisher_->publish(array);
    }

    gz::transport::Node gz_node_;

    rclcpp::Publisher<
        chocolate_interfaces::msg::ChocolatePoseArray>::SharedPtr publisher_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<ChocolateTracking>();

    rclcpp::spin(node);

    rclcpp::shutdown();

    return 0;
}
