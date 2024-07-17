# Import the rclpy library, which provides the ROS 2 Python client library
import rclpy

# Import the Node class from rclpy.node, which provides the base class for all ROS 2 nodes
from rclpy.node import Node

# Import the String message type from the std_msgs package
from std_msgs.msg import String

# Define a class MinimalPublisher which inherits from Node
class MinimalPublisher(Node):
    def __init__(self):
        # Initialize the node by calling the superclass constructor with the name 'minimal_publisher'
        super().__init__('minimal_publisher')
        
        # Create a publisher that publishes String messages to the 'topic' topic
        # The queue size is set to 10, which means the publisher can store up to 10 messages in the queue
        # before starting to discard old ones if new messages keep coming in faster than they can be sent out.
        self.publisher_ = self.create_publisher(
            String,   # The type of message the publisher will send
            'topic',  # The name of the topic
            10        # The queue size
        )
        
        # Set the timer period to 2 seconds
        timer_period = 2.0
        
        # Create a timer that calls the timer_callback function every 2 seconds
        # self.create_timer takes the period (in seconds) and the callback function as arguments
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Initialize a counter to keep track of the number of messages published
        self.i = 0

    # Define the timer callback function that will be called every 2 seconds
    def timer_callback(self):
        # Create a new String message
        msg = String()
        
        # Set the message data to a string that includes the current count value
        msg.data = f'Hello, this is message {self.i}'
        
        # Publish the message to the 'topic' topic
        self.publisher_.publish(msg)
        
        # Log the message data to the console for debugging and monitoring purposes
        self.get_logger().info(f'Publishing: "{msg.data}"')
        
        # Increment the counter for the next message
        self.i += 1

# Define the main function
def main(args=None):
    # Initialize the rclpy library. This prepares the ROS 2 environment for running nodes.
    rclpy.init(args=args)
    
    # Create an instance of the MinimalPublisher node
    minimal_publisher = MinimalPublisher()
    
    # Spin the node so its callbacks are called (i.e., keep it alive and responsive).
    # This function will block and keep the node running, handling all callbacks and events.
    rclpy.spin(minimal_publisher)
    
    # Clean up and destroy the node. This is called after rclpy.spin() is stopped (e.g., with Ctrl+C).
    minimal_publisher.destroy_node()
    
    # Shutdown the rclpy library to free up resources.
    rclpy.shutdown()

# Check if the script is being run directly (as opposed to being imported as a module).
if __name__ == '__main__':
    # If so, call the main function to start the node.
    main()
