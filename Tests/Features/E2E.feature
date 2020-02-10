Feature: Checkout basic flow

  @E2E
  Scenario: Rent a car basic flow - positive
    Given User go to the search page
    And User fill all mandatory fields
    And User click Search button
    And User check if form return proper results for our search setup
    And User chose one option from the list and click Rent
    And User check if the next page has proper value
    And User click button Rent1
    And User check if all information on the Summary are proper
    And User fill all mandatory fields on Summary step
    When User click button Rent
    Then User should receive confirmation regarding rent offer