# Testing Strategy

The aim of the testing strategy of the Quick-Calc app is to ensure that the calculator's core features are functioning correctly. We have divided the tests into unit tests and integration tests so that we may check the correctness of individual functions as well as the interactions of the system.

First, unit tests check different simple calculator functions like addition, subtraction, multiplication, and division only. These tests are used to confirm that each function performs correctly when given different inputs including boundary cases.

Integration tests make sure that several parts of the system work together as expected. Here, they represent the user interacting with the calculator's logic which is why they check if the app returns the right output.

---

# Testing Pyramid

The testing pyramid suggests having many unit tests, fewer integration tests, and even fewer end-to-end tests. This project follows the pyramid by including multiple unit tests for the core calculation logic and a smaller number of integration tests that verify interactions between system components.

---

# Black Box vs White Box Testing

Unit tests in this project follow a **white-box testing approach** because they directly test the internal methods of the calculator class.

Integration tests follow a **black-box testing approach** because they verify the overall behavior of the system without focusing on the internal implementation details.

---

# Functional vs Non-Functional Testing

Functional Testing is the test that this project implemented to makes sure that the calculator is working correctly while performing the operations.

Non-functional testing like performance testing, usability testing, and security testing are not considered in this project because the assignment is very specific to functionality correctness verification only.

---

# Regression Testing

Regression testing is the process of making sure that the newly introduced changes have not deleted or changed the existing feature, without the user's knowledge. The present test collection will serve the purpose of validation of new addition of feature, unchanged functionality of previous feature.

---

# Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_full_user_flow | Integration | Pass |
| test_clear_function | Integration | Pass |
