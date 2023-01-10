Feature: Google

  Scenario: Log in to google account
    Given User have open google website
    When Click on the log in button
    When User set login field
    When User click on the next button
    When User set password field
    When User click on the next button
    Then User is logged in
