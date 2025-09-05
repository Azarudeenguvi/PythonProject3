from Task16.Pages.population import Population

url='https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live'
def test_population(driver):
    driver.get(url)
    count=Population(driver)
    count.counting_population()
    while True:
        count.counting_population()



