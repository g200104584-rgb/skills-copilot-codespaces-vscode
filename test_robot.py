"""
Simple tests for the Rux robot
"""

import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from robot import Robot


def test_robot_creation():
    """Test that robot can be created"""
    robot = Robot(name="TestRux")
    assert robot.name == "TestRux"
    assert robot.mood == "happy"
    print("✓ test_robot_creation passed")


def test_greeting():
    """Test greeting functionality"""
    robot = Robot()
    greeting = robot.greet()
    assert isinstance(greeting, str)
    assert len(greeting) > 0
    assert robot.name in greeting or "Hello" in greeting or "Hi" in greeting
    print("✓ test_greeting passed")


def test_respond():
    """Test response functionality"""
    robot = Robot()
    response = robot.respond("Hello")
    assert isinstance(response, str)
    assert len(response) > 0
    print("✓ test_respond passed")


def test_learn():
    """Test learning functionality"""
    robot = Robot()
    initial_count = sum(len(responses) for responses in robot.knowledge_base.values())
    
    result = robot.learn("test_category", "test response")
    
    new_count = sum(len(responses) for responses in robot.knowledge_base.values())
    assert new_count == initial_count + 1
    assert "test_category" in robot.knowledge_base
    assert "test response" in robot.knowledge_base["test_category"]
    print("✓ test_learn passed")


def test_mood():
    """Test mood system"""
    robot = Robot()
    result = robot.set_mood("excited")
    assert robot.mood == "excited"
    assert "excited" in result
    print("✓ test_mood passed")


def test_stats():
    """Test statistics"""
    robot = Robot()
    stats = robot.get_stats()
    
    assert "name" in stats
    assert "mood" in stats
    assert "knowledge_categories" in stats
    assert "total_responses" in stats
    assert stats["name"] == "Rux"
    print("✓ test_stats passed")


def test_conversation_history():
    """Test conversation history"""
    robot = Robot()
    
    # Initially should be empty or have system messages
    initial_length = len(robot.get_conversation_history())
    
    # Have some interactions
    robot.respond("Hello")
    robot.respond("How are you?")
    
    # Should have more entries
    history = robot.get_conversation_history()
    assert len(history) > initial_length
    
    # Check structure
    if len(history) > 0:
        entry = history[0]
        assert "timestamp" in entry
        assert "sender" in entry
        assert "message" in entry
    
    print("✓ test_conversation_history passed")


def test_save_load_knowledge():
    """Test saving and loading knowledge"""
    robot1 = Robot()
    robot1.learn("unique_test", "unique response")
    
    # Save
    filename = "test_robot_knowledge.json"
    robot1.save_knowledge(filename)
    
    # Load in new robot
    robot2 = Robot()
    robot2.load_knowledge(filename)
    
    # Check that knowledge was transferred
    assert "unique_test" in robot2.knowledge_base
    assert "unique response" in robot2.knowledge_base["unique_test"]
    
    # Cleanup
    if os.path.exists(filename):
        os.remove(filename)
    
    print("✓ test_save_load_knowledge passed")


def test_farewell():
    """Test farewell functionality"""
    robot = Robot()
    farewell = robot.farewell()
    assert isinstance(farewell, str)
    assert len(farewell) > 0
    print("✓ test_farewell passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*50)
    print("Running Rux Robot Tests")
    print("="*50 + "\n")
    
    tests = [
        test_robot_creation,
        test_greeting,
        test_respond,
        test_learn,
        test_mood,
        test_stats,
        test_conversation_history,
        test_save_load_knowledge,
        test_farewell
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("\n" + "="*50)
    print(f"Results: {passed} passed, {failed} failed")
    print("="*50 + "\n")
    
    if failed == 0:
        print("🎉 All tests passed!")
        return 0
    else:
        print(f"❌ {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
