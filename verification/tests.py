"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [["flower", "flow", "flight"]],
            "answer": "fl"
        },
        {
            "input": [["dog", "racecar", "car"]],
            "answer": ""
        },
        {
            "input": [["apple", "application", "appetizer"]],
            "answer": "app"
        },
        {
            "input": [["a"]],
            "answer": "a"
        },
        {
            "input": [["", "b"]],
            "answer": ""
        },
        {
            "input": [["same", "same", "same"]],
            "answer": "same"
        },
        {
            "input": [["mismatch", "mister", "miss"]],
            "answer": "mis"
        },
        {
            "input": [["alphabet", "alpha", "alphadog"]],
            "answer": "alpha"
        },
        {
            "input": [["book", "boot", "booster"]],
            "answer": "boo"
        },
        {
            "input": [["short", "shore", "shot"]],
            "answer": "sho"
        },
    ],
    "Extra": [
        {
            "input": [["interspace", "interface", "interstellar", "intersperse"]],
            "answer": "inter"
        },
        {
            "input": [["sunflower", "sunday", "sundial"]],
            "answer": "sun"
        },
    ]
}
