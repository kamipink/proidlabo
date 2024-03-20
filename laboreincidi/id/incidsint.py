def num_results_greater_than_zero(driver):
  results = driver.find_elements_by_class_name("results")
  return len(results) > 0

WebDriverWait(driver, 10).until(num_results_greater_than_zero)
