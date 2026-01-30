"""
Rux-like Robot Implementation
A conversational robot built from scratch with learning capabilities
"""

import json
import random
from datetime import datetime
from typing import Dict, List, Optional


class Robot:
    """A conversational robot with basic AI capabilities"""
    
    def __init__(self, name: str = "Rux"):
        """
        Initialize the robot
        
        Args:
            name: The robot's name (default: "Rux")
        """
        self.name = name
        self.knowledge_base: Dict[str, List[str]] = {}
        self.conversation_history: List[Dict[str, str]] = []
        self.created_at = datetime.now()
        self.mood = "happy"
        
        # Initialize with basic knowledge
        self._initialize_knowledge()
    
    def _initialize_knowledge(self):
        """Initialize robot with basic knowledge and responses"""
        self.knowledge_base = {
            "greeting": [
                f"Hello! I'm {self.name}, your friendly robot assistant!",
                f"Hi there! {self.name} at your service!",
                f"Greetings! I'm {self.name}, how can I help you today?"
            ],
            "farewell": [
                "Goodbye! It was nice talking to you!",
                "See you later! Have a great day!",
                "Bye! Come back soon!"
            ],
            "help": [
                "I can chat with you, learn new things, and remember our conversations!",
                "I'm here to assist you. You can teach me new responses or just have a conversation!",
                "I can greet you, say goodbye, and learn from our interactions!"
            ],
            "thanks": [
                "You're welcome!",
                "Happy to help!",
                "My pleasure!"
            ],
            "name": [
                f"My name is {self.name}!",
                f"I'm {self.name}, a robot built from scratch!",
                f"You can call me {self.name}!"
            ],
            "how_are_you": [
                f"I'm feeling {self.mood}! Thanks for asking!",
                "I'm doing great! How about you?",
                "All systems operational! I'm doing well!"
            ],
            "default": [
                "That's interesting! Tell me more.",
                "I'm learning new things every day!",
                "Thanks for sharing that with me!",
                "I'll remember that for our future conversations."
            ]
        }
    
    def greet(self) -> str:
        """Generate a greeting message"""
        response = random.choice(self.knowledge_base["greeting"])
        self._log_interaction("system", response)
        return response
    
    def farewell(self) -> str:
        """Generate a farewell message"""
        response = random.choice(self.knowledge_base["farewell"])
        self._log_interaction("system", response)
        return response
    
    def respond(self, user_input: str) -> str:
        """
        Respond to user input
        
        Args:
            user_input: The user's message
            
        Returns:
            The robot's response
        """
        self._log_interaction("user", user_input)
        
        # Normalize input
        user_input_lower = user_input.lower().strip()
        
        # Check for different types of input
        if any(word in user_input_lower for word in ["hi", "hello", "hey", "greetings"]):
            response = random.choice(self.knowledge_base["greeting"])
        elif any(word in user_input_lower for word in ["bye", "goodbye", "see you"]):
            response = random.choice(self.knowledge_base["farewell"])
        elif any(word in user_input_lower for word in ["help", "what can you do"]):
            response = random.choice(self.knowledge_base["help"])
        elif any(word in user_input_lower for word in ["thanks", "thank you"]):
            response = random.choice(self.knowledge_base["thanks"])
        elif any(word in user_input_lower for word in ["your name", "who are you"]):
            response = random.choice(self.knowledge_base["name"])
        elif any(word in user_input_lower for word in ["how are you", "how do you feel"]):
            response = random.choice(self.knowledge_base["how_are_you"])
        else:
            response = random.choice(self.knowledge_base["default"])
        
        self._log_interaction("robot", response)
        return response
    
    def learn(self, category: str, response: str) -> str:
        """
        Teach the robot a new response
        
        Args:
            category: The category for the response
            response: The new response to add
            
        Returns:
            Confirmation message
        """
        if category not in self.knowledge_base:
            self.knowledge_base[category] = []
        
        self.knowledge_base[category].append(response)
        return f"Thanks! I've learned a new {category} response!"
    
    def _log_interaction(self, sender: str, message: str):
        """Log an interaction to the conversation history"""
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "sender": sender,
            "message": message
        })
    
    def get_stats(self) -> Dict:
        """Get robot statistics"""
        return {
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "mood": self.mood,
            "knowledge_categories": len(self.knowledge_base),
            "total_responses": sum(len(responses) for responses in self.knowledge_base.values()),
            "conversation_length": len(self.conversation_history)
        }
    
    def save_knowledge(self, filename: str = "robot_knowledge.json"):
        """Save knowledge base to a file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge_base, f, indent=2, ensure_ascii=False)
        return f"Knowledge saved to {filename}"
    
    def load_knowledge(self, filename: str = "robot_knowledge.json"):
        """Load knowledge base from a file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.knowledge_base = json.load(f)
            return f"Knowledge loaded from {filename}"
        except FileNotFoundError:
            return f"File {filename} not found. Using default knowledge."
    
    def set_mood(self, mood: str):
        """Set the robot's mood"""
        self.mood = mood
        return f"My mood is now: {mood}"
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get the conversation history"""
        return self.conversation_history


def main():
    """Main function to demonstrate the robot"""
    print("=" * 50)
    print("Welcome to the Rux-like Robot Demo!")
    print("=" * 50)
    
    # Create a robot
    robot = Robot(name="Rux")
    
    # Greet the user
    print(f"\n{robot.greet()}\n")
    
    # Interactive conversation loop
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type 'stats' to see robot statistics")
    print("Type 'learn <category> <response>' to teach the robot")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit']:
            print(f"\n{robot.name}: {robot.farewell()}")
            break
        
        if user_input.lower() == 'stats':
            stats = robot.get_stats()
            print(f"\n{robot.name} Statistics:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
            continue
        
        if user_input.lower().startswith('learn '):
            parts = user_input.split(' ', 2)
            if len(parts) >= 3:
                category = parts[1]
                response = parts[2]
                print(f"\n{robot.name}: {robot.learn(category, response)}")
            else:
                print(f"\n{robot.name}: Please use: learn <category> <response>")
            continue
        
        # Regular conversation
        response = robot.respond(user_input)
        print(f"\n{robot.name}: {response}")
    
    # Show final stats
    print("\n" + "=" * 50)
    print("Final Statistics:")
    stats = robot.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    print("=" * 50)


if __name__ == "__main__":
    main()
