# Tutorials

## Checking validity

### Check if states are valid

```
check_states = check_valid_states(
    selected_states = "'Kerala', 'Bihar'"
)
```

## Fetching data

### Get a list of districts in a specific state

```
district_list = get_districts(
    selected_states = "'Kerala', 'Bihar'"
)
```

### Fetch reservoirs in a specific state and district

```
reservoirs = get_reservoirs(
    end_date = 2024-01-30,
    selected_states = "Kerala",
    selected_districts = "Wayanad"
)
```

### Get available date range for reservoir data {wip}

### Get the information on a specific resrvoir

```
res_info = get_reservoir_info(
    reservoir_name_str = "'Mahi Bajaj Sagar', 'Jawai Dam'"
)
```

### Get the names of reservoirs in a specific state and district

```
res_names = get_reservoir_names(
    states_list_str = "'Tamil Nadu', 'Punjab'"
    districts_names_list_str = "'Coimbatore', 'Patiala', 'Salem'"
)
```

## Plotting

### General plot {wip}

```
plot_object = plot_data(
    input_object = ''
)
```

### Interactive timeseries plot without specifying columns

```
plot_timeseries - plot_reservoir(
    title = "An interactive timeseries plot"
)
```

## Hydroframe

### List reservoirs currently in hydroframe

```
hf1.reservoirs
```

### Plot timeseries data for a specific reservoir

```
hf1.reservoir['Idamalayar Reservoir'].plot()
```