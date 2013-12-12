Feature: Todo List
    As a user I want to be able to create a new todo
    and view a todo task

    Scenario: create a new todo
        Given my todo is "new todo task"
        When I create a new todo entry
        Then I should find todo in todo table

    Scenario: view a todo task
        Given my todo is "another todo task"
        When I create a new todo entry
        And I visit the URL /1
        Then I should see my todo
