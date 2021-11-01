Feature: Comments
  # In scope of feature will be covered API test cases of "product" functionality

  Scenario: Check emails from comments
    Given user with name Delphine
    When get posts for user
    Then validate emails from comments
