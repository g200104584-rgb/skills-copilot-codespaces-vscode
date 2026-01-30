"""
Example script demonstrating the Rux robot capabilities
This script shows various features and use cases
"""

from robot import Robot
import time


def demo_basic_conversation():
    """Demo 1: Basic conversation capabilities"""
    print("\n" + "="*60)
    print("DEMO 1: Basic Conversation")
    print("="*60)
    
    robot = Robot(name="Rux")
    
    # Greeting
    print(f"\nRobot: {robot.greet()}")
    time.sleep(1)
    
    # Various interactions
    interactions = [
        "Hello!",
        "How are you?",
        "What can you do?",
        "Thanks for your help!"
    ]
    
    for user_msg in interactions:
        print(f"\nUser: {user_msg}")
        time.sleep(0.5)
        print(f"Robot: {robot.respond(user_msg)}")
        time.sleep(1)
    
    # Farewell
    print(f"\nUser: Goodbye!")
    time.sleep(0.5)
    print(f"Robot: {robot.farewell()}")


def demo_learning_capability():
    """Demo 2: Teaching the robot new responses"""
    print("\n" + "="*60)
    print("DEMO 2: Learning Capability")
    print("="*60)
    
    robot = Robot(name="Rux")
    
    print(f"\nRobot: {robot.greet()}")
    time.sleep(1)
    
    # Teach the robot new things
    print("\n--- Teaching the robot new responses ---")
    
    learning_examples = [
        ("joke", "Why did the robot go to therapy? It had too many bugs!"),
        ("joke", "What do you call a robot that takes the long way around? R2-Detour!"),
        ("fact", "Did you know? The first industrial robot was called Unimate!"),
        ("fact", "Robots can work in environments too dangerous for humans!"),
    ]
    
    for category, response in learning_examples:
        print(f"\nTeaching: Category='{category}', Response='{response[:50]}...'")
        time.sleep(0.5)
        result = robot.learn(category, response)
        print(f"Robot: {result}")
        time.sleep(1)
    
    print("\n--- Robot has learned new responses! ---")


def demo_statistics():
    """Demo 3: Robot statistics and information"""
    print("\n" + "="*60)
    print("DEMO 3: Statistics and Information")
    print("="*60)
    
    robot = Robot(name="Rux")
    
    # Generate some activity
    robot.greet()
    robot.respond("Hello!")
    robot.respond("How are you?")
    robot.learn("custom", "This is a custom response!")
    
    # Display statistics
    print("\n--- Robot Statistics ---")
    stats = robot.get_stats()
    for key, value in stats.items():
        print(f"{key:.<30} {value}")
    
    time.sleep(2)


def demo_conversation_history():
    """Demo 4: Conversation history tracking"""
    print("\n" + "="*60)
    print("DEMO 4: Conversation History")
    print("="*60)
    
    robot = Robot(name="Rux")
    
    # Have a conversation
    robot.greet()
    robot.respond("Hi there!")
    robot.respond("Tell me about yourself")
    robot.respond("That's cool!")
    
    # Show conversation history
    print("\n--- Conversation History ---")
    history = robot.get_conversation_history()
    
    for i, interaction in enumerate(history, 1):
        sender = interaction['sender'].upper()
        message = interaction['message']
        timestamp = interaction['timestamp'].split('T')[1].split('.')[0]
        print(f"{i}. [{timestamp}] {sender}: {message}")
        time.sleep(0.3)


def demo_mood_system():
    """Demo 5: Mood system"""
    print("\n" + "="*60)
    print("DEMO 5: Mood System")
    print("="*60)
    
    robot = Robot(name="Rux")
    
    moods = ["happy", "excited", "thoughtful", "cheerful", "curious"]
    
    print("\n--- Testing different moods ---")
    for mood in moods:
        print(f"\nSetting mood to: {mood}")
        result = robot.set_mood(mood)
        print(f"Robot: {result}")
        time.sleep(0.5)
        
        # Ask how the robot is doing
        response = robot.respond("How are you?")
        print(f"Robot: {response}")
        time.sleep(1)


def demo_persistence():
    """Demo 6: Saving and loading knowledge"""
    print("\n" + "="*60)
    print("DEMO 6: Knowledge Persistence")
    print("="*60)
    
    filename = "demo_knowledge.json"
    
    # Create first robot and teach it
    print("\n--- Creating and teaching Robot 1 ---")
    robot1 = Robot(name="Rux")
    robot1.learn("special", "I know something special!")
    robot1.learn("special", "This is unique knowledge!")
    
    print("Robot 1 learned special knowledge")
    time.sleep(1)
    
    # Save knowledge
    print("\n--- Saving knowledge to file ---")
    result = robot1.save_knowledge(filename)
    print(f"Robot 1: {result}")
    time.sleep(1)
    
    # Create second robot and load knowledge
    print("\n--- Creating Robot 2 and loading knowledge ---")
    robot2 = Robot(name="Rux2")
    result = robot2.load_knowledge(filename)
    print(f"Robot 2: {result}")
    time.sleep(1)
    
    # Show that robot2 has the same knowledge
    print("\n--- Robot 2 now has Robot 1's knowledge! ---")
    stats = robot2.get_stats()
    print(f"Total responses in knowledge base: {stats['total_responses']}")
    
    # Cleanup
    import os
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\n--- Cleaned up {filename} ---")
    

def demo_advanced_usage():
    """Demo 7: Advanced programmatic usage"""
    print("\n" + "="*60)
    print("DEMO 7: Advanced Programmatic Usage")
    print("="*60)
    
    robot = Robot(name="AdvancedRux")
    
    print("\n--- Creating a specialized robot ---")
    
    # Add specialized knowledge
    specialized_topics = {
        "programming": [
            "Python is a great language for beginners!",
            "I love coding in Python!",
            "Variables store data in programming."
        ],
        "math": [
            "Math is the language of the universe!",
            "2 + 2 = 4, quick maths!",
            "Geometry studies shapes and spaces."
        ],
        "science": [
            "Science helps us understand the world!",
            "Physics explains how things move!",
            "Chemistry is about matter and reactions!"
        ]
    }
    
    for topic, responses in specialized_topics.items():
        for response in responses:
            robot.learn(topic, response)
        print(f"✓ Loaded {topic} knowledge")
        time.sleep(0.3)
    
    print(f"\n--- Specialized robot created with {robot.get_stats()['total_responses']} total responses ---")


def main():
    """Run all demonstrations"""
    print("\n" + "#"*60)
    print("#" + " "*58 + "#")
    print("#" + " "*15 + "RUX ROBOT DEMO SUITE" + " "*23 + "#")
    print("#" + " "*58 + "#")
    print("#"*60)
    
    demos = [
        ("Basic Conversation", demo_basic_conversation),
        ("Learning Capability", demo_learning_capability),
        ("Statistics", demo_statistics),
        ("Conversation History", demo_conversation_history),
        ("Mood System", demo_mood_system),
        ("Knowledge Persistence", demo_persistence),
        ("Advanced Usage", demo_advanced_usage)
    ]
    
    print("\nAvailable Demos:")
    for i, (name, _) in enumerate(demos, 1):
        print(f"  {i}. {name}")
    
    print("\n" + "-"*60)
    choice = input("\nEnter demo number (1-7) or 'all' to run all demos: ").strip().lower()
    
    if choice == 'all':
        for name, demo_func in demos:
            demo_func()
            time.sleep(2)
    elif choice.isdigit() and 1 <= int(choice) <= len(demos):
        demos[int(choice) - 1][1]()
    else:
        print("Invalid choice. Running all demos...")
        for name, demo_func in demos:
            demo_func()
            time.sleep(2)
    
    print("\n" + "#"*60)
    print("#" + " "*58 + "#")
    print("#" + " "*18 + "DEMO COMPLETE!" + " "*27 + "#")
    print("#" + " "*58 + "#")
    print("#"*60)
    print("\nThank you for exploring the Rux robot! 🤖")


if __name__ == "__main__":
    main()
