# Rux-like Robot - Built from Scratch

A conversational robot implementation with learning capabilities, built from scratch in Python.

## Overview

This robot (Rux) is a friendly conversational AI assistant that can:
- Engage in natural conversations
- Learn new responses from interactions
- Remember conversation history
- Save and load knowledge base
- Display statistics about interactions

## Features

### Core Capabilities
1. **Conversational Interface**: Natural language interaction with the robot
2. **Learning System**: Teach the robot new responses in different categories
3. **Knowledge Base**: Pre-loaded with basic conversational knowledge
4. **Mood System**: The robot has a mood that affects its responses
5. **Conversation History**: Tracks all interactions with timestamps
6. **Persistence**: Save and load knowledge base to/from JSON files

### Built-in Knowledge Categories
- **greeting**: Various ways to say hello
- **farewell**: Different goodbye messages
- **help**: Information about robot capabilities
- **thanks**: Responses to gratitude
- **name**: Information about the robot's identity
- **how_are_you**: Responses about the robot's status
- **default**: General responses for unknown inputs

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. No additional dependencies required (uses only Python standard library)

```bash
cd skills-copilot-codespaces-vscode
python robot.py
```

## Usage

### Running the Robot

#### Interactive Mode (Recommended)
```bash
python robot.py
```

This launches an interactive conversation session where you can:
- Chat with the robot
- Type `quit` or `exit` to end the conversation
- Type `stats` to see robot statistics
- Type `learn <category> <response>` to teach new responses

#### Programmatic Usage
```python
from robot import Robot

# Create a robot instance
robot = Robot(name="Rux")

# Greet
print(robot.greet())

# Have a conversation
response = robot.respond("Hello!")
print(response)

# Teach the robot something new
robot.learn("joke", "Why did the robot cross the road? To get to the other side!")

# Check statistics
stats = robot.get_stats()
print(stats)

# Save knowledge
robot.save_knowledge("my_robot_knowledge.json")

# Load knowledge
robot.load_knowledge("my_robot_knowledge.json")
```

### Examples

#### Example 1: Basic Conversation
```
You: Hello!
Rux: Hi there! Rux at your service!

You: How are you?
Rux: I'm feeling happy! Thanks for asking!

You: What can you do?
Rux: I can chat with you, learn new things, and remember our conversations!

You: Thanks!
Rux: You're welcome!
```

#### Example 2: Teaching the Robot
```
You: learn joke Why did the robot go to school? To improve its AI!
Rux: Thanks! I've learned a new joke response!
```

#### Example 3: Viewing Statistics
```
You: stats

Rux Statistics:
  name: Rux
  created_at: 2026-01-30T01:20:00.000000
  mood: happy
  knowledge_categories: 7
  total_responses: 21
  conversation_length: 8
```

## Architecture

### Class Structure

```
Robot
├── __init__(name)           # Initialize the robot
├── greet()                  # Generate greeting
├── farewell()               # Generate farewell
├── respond(user_input)      # Process and respond to input
├── learn(category, response) # Add new knowledge
├── get_stats()              # Get robot statistics
├── save_knowledge(filename) # Save knowledge to file
├── load_knowledge(filename) # Load knowledge from file
├── set_mood(mood)           # Change robot's mood
└── get_conversation_history() # Get conversation log
```

### Knowledge Base Structure

The knowledge base is organized as a dictionary:
```python
{
  "category_name": [
    "response_1",
    "response_2",
    "response_3"
  ]
}
```

### Conversation History

Each interaction is logged with:
- `timestamp`: ISO format datetime
- `sender`: "user", "robot", or "system"
- `message`: The actual message content

## Configuration

The robot can be configured using `robot_config.json`:

```json
{
  "robot_settings": {
    "default_name": "Rux",
    "default_mood": "happy",
    "enable_learning": true,
    "save_conversations": true
  },
  "personality": {
    "friendly": true,
    "helpful": true,
    "curious": true
  }
}
```

## Customization

### Adding New Response Categories

```python
robot = Robot()
robot.learn("weather", "The weather is great today!")
robot.learn("weather", "I hope it's sunny where you are!")
```

### Changing Robot Mood

```python
robot.set_mood("excited")
robot.set_mood("thoughtful")
robot.set_mood("cheerful")
```

### Saving Progress

```python
# Save after learning new things
robot.save_knowledge("custom_knowledge.json")

# Load in a future session
robot.load_knowledge("custom_knowledge.json")
```

## Advanced Features

### Conversation History Analysis

```python
# Get full conversation history
history = robot.get_conversation_history()

# Analyze conversations
for interaction in history:
    print(f"{interaction['timestamp']}: {interaction['sender']} - {interaction['message']}")
```

### Custom Response Patterns

The robot uses keyword matching for responses. You can extend this by:
1. Adding more keywords to existing categories
2. Creating new categories with specific keywords
3. Implementing more sophisticated NLP if needed

## Technical Details

- **Language**: Python 3.7+
- **Dependencies**: None (uses only standard library)
- **Data Storage**: JSON for knowledge persistence
- **Response Selection**: Random selection from category responses

## Future Enhancements

Potential improvements for the robot:
- [ ] Natural Language Processing (NLP) for better understanding
- [ ] Machine Learning for response generation
- [ ] Multi-language support
- [ ] Voice interface
- [ ] Web interface
- [ ] Database integration
- [ ] API endpoints
- [ ] Context-aware responses
- [ ] Sentiment analysis

## Troubleshooting

### Common Issues

1. **Robot doesn't understand input**
   - The robot uses simple keyword matching
   - Try different phrasings or teach it new responses

2. **Knowledge not persisting**
   - Make sure to call `save_knowledge()` before exiting
   - Check file permissions for writing JSON files

3. **Import errors**
   - Ensure you're using Python 3.7+
   - No external dependencies should be needed

## Contributing

To improve the robot:
1. Fork the repository
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is open source and available for educational purposes.

## Credits

Built from scratch as a learning project for conversational AI and robotics concepts.

---

**Happy Robot Building! 🤖**
