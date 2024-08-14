#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStationNode: public rclcpp::Node
{
public:
    RobotNewsStationNode(): Node("robot_news_station")
    {
        
        RCLCPP_INFO(this->get_logger(), "Hello Cpp Node)");
    }

private:
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;

};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}