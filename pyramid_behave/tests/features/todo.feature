Feature: Create todo
    In order to have a todo in my todo list
    As a user
    I will create a new todo

    Scenario: create a new todo
        Given my task is "new todo task"
        When I create a new todo entry
        Then I should find todo in todo table

