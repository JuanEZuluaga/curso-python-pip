import utils
import read_csv
import charts


def main():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country'], data))
  percentage = list(map(lambda x: x['World Population Percentage'], data))
  # labels, values = utils.get_world_percentages(data)
  charts.generate_pie_chart(countries, percentage)
  # data = read_csv.read_csv('./app/data.csv')
  country = input('Type country: ')
  selected_country = utils.get_population_by_country(data, country)
  if len(selected_country) > 0:
    labels, values = utils.get_population(selected_country[0])
    charts.generate_bar_chart(country,labels, values)
  else:
    print('el pais no esta disponible')


if __name__ == '__main__':
  main()
