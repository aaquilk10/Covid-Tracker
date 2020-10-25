import numpy as np
import pandas as pd
import us
import ExtractData as extract
import matplotlib.pyplot as plt

pd.set_option('max_columns', None)
pd.set_option('max_rows', None)


class CovidTracker:
    def __init__(self):
        self.url = "https://api.covidtracking.com/v1/"
        self.entire_us = "us/current.csv"
        self.all_states = "states/current.csv"
        self.data = 0

    def get_state(self, name):
        return "states/{}/current.csv".format(us.states.lookup(name).abbr.lower())

    def us_data(self):
        self.data = extract.CovidData(self.url + self.entire_us).data()
        print(self.data[["positive", "positiveIncrease", "hospitalized", "hospitalizedIncrease", "recovered", "death",
                         "deathIncrease"]])
        while True:
            user_input = input("Enter 'Plot' to plot the data, 'Back' to go back, or 'Exit' to exit: ").lower()
            if user_input == "back":
                self.start()
                break
            elif user_input == 'exit':
                exit()
            elif user_input == 'plot':
                labels = ["positive", "positiveIncrease", "hospitalized", "hospitalizedIncrease", "recovered", "death",
                          "deathIncrease"]
                df = pd.DataFrame(self.data[labels])
                df.plot.bar()
                plt.show()
            else:
                print("Please enter a valid parameter")

    def states_data(self):
        self.data = extract.CovidData(self.url + self.all_states).data()
        print(self.data[["state", "positive", "positiveIncrease", "hospitalized", "hospitalizedIncrease", "recovered",
                         "death", "deathIncrease"]])
        while True:
            user_input = input("Enter 'Back' to go back, or 'Exit' to exit: ").lower()
            if user_input == "back":
                self.start()
                break
            elif user_input == 'exit':
                exit()
            else:
                print("Please enter a valid parameter")

    def sp_state_data(self, state_url):
        self.data = extract.CovidData(state_url).data()
        print(self.data[["state", "positive", "positiveIncrease", "hospitalized", "hospitalizedIncrease", "recovered",
                         "death", "deathIncrease"]])
        while True:
            user_input = input("Enter 'Plot' to plot the data, 'Back' to go back, or 'Exit' to exit: ").lower()
            if user_input == "back":
                self.start()
                break
            elif user_input == 'exit':
                exit()
            elif user_input == 'plot':
                labels = ["state", "positive", "positiveIncrease", "hospitalized", "hospitalizedIncrease", "recovered",
                          "death", "deathIncrease"]
                df = pd.DataFrame(self.data[labels])
                df.plot.bar()
                plt.show()
            else:
                print("Please enter a valid parameter")

    def start(self):
        while True:
            user_in = input("Type 'US' for a summary, 'States' for data of all states, name of a state to get data for"
                            " that state, or 'Exit' to exit: ").lower()
            if user_in == 'exit':
                exit()
            elif user_in == "us":
                self.us_data()
                break
            elif user_in == "states":
                self.states_data()
                break
            else:
                try:
                    state_url = self.url + self.get_state(user_in)
                    self.sp_state_data(state_url)
                    break
                except AttributeError:
                    print("Please enter a valid parameter")


if __name__ == '__main__':
    app = CovidTracker()
    app.start()
