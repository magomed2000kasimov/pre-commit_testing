Feature: search Cheese

  Scenario: Cheese
    Given I am on the Google search page
      When I search for "Cheese"
      Then hen the page title should start with "cheese"
      And quit browser
