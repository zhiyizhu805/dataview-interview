from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

# Reading data
data_df = pd.read_csv("static/data/Pests.csv")


@app.route('/')
def index():
    return render_template('index.html')


def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""
    percent = np.round((np.divide(val, total) * 100), 2)
    return percent


def data_creation(data, percent, class_labels, group=None):
    for index, item in enumerate(percent):
        data_instance = {}
        data_instance['category'] = class_labels[index]
        data_instance['value'] = item
        data_instance['group'] = group
        data.append(data_instance)


@app.route('/get_piechart_data')
def get_piechart_data():
    year_labels = ['2020', '2021', '2022']
    _ = data_df.groupby('year')['count'].sum().values
    # Getting the value counts and total
    class_percent = calculate_percentage(_, np.sum(_))

    piechart_data = []
    data_creation(piechart_data, class_percent, year_labels)
    return jsonify(piechart_data)


@app.route('/get_barchart_data')
def get_barchart_data():
    pest_labels = ['Bird', 'Cat', 'Ferret', 'Hedgehog', 'Magpie', 'Mouse', 'Other', 'Possum',
                   'Rabbit', 'Rat', 'Rat - ship', 'Rat - norway', 'Stoat', 'Unspecified', 'Weasel', 'PÅ«keko']
    year_2020 = data_df[data_df['year'] == 2020]
    year_2021 = data_df[data_df['year'] == 2021]
    year_2022 = data_df[data_df['year'] == 2022]
    _ = year_2020.groupby('Type', observed=False)['count'].sum().values
    y2020_percent = calculate_percentage(_, np.sum(_))
    _ = year_2021.groupby('Type', observed=False)['count'].sum().values
    y2021_percent = calculate_percentage(_, np.sum(_))
    _ = year_2022.groupby('Type', observed=False)['count'].sum().values
    y2022_percent = calculate_percentage(_, np.sum(_))
    _ = data_df.groupby('Type', observed=False)['count'].sum().values
    all_percent = calculate_percentage(_, np.sum(_))

    barchart_data = []
    data_creation(barchart_data, all_percent, pest_labels, "All")
    data_creation(barchart_data, y2020_percent, pest_labels, "2020")
    data_creation(barchart_data, y2021_percent, pest_labels, "2021")
    data_creation(barchart_data, y2022_percent, pest_labels, "2022")
    return jsonify(barchart_data)


if __name__ == '__main__':
    app.run(debug=True)
