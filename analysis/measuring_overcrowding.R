library(plotly)

plotly_barchart_of_pcts <- function(df, path_to_save=NULL, overwrite=FALSE) {
  num_institutions <- length(unique(df$institution_name))
  font_for_labels <- list(color = '#cdc5bf',
                          family = 'sans serif',
                          size = 12)
  
  in_order <- df %>% arrange(percent_occupied)
  order_level <- in_order$institution_name
  df$factor_name <- factor(df$institution_name, levels = order_level)
  # This is probably more confusing than it needs to be, but basically we want the damn thing to be in order based
  # on the `percent_occupied` value. This does that.
  df <- df %>% arrange(factor_name)
  
  p <- df %>%
    plot_ly() %>%
    add_trace(
      x = ~percent_occupied,
      y = ~factor_name,
      type = "bar",
      hoverinfo = 'text',
      text = ~paste(
        'Institution: ',
        institution_name,
        '<br>',
        'Capacity: ', designed_capacity, ', Actual: ', total_population,
        '<br>',
        percent_occupied,
        '% occupied',
        sep = ''
      )
  ) %>%
    add_annotations(
      # All the way to the left
      x = 0,
      y = ~institution_name,
      text = ~institution_name,
      # See https://github.com/plotly/plotly.js/blob/master/src/components/annotations/attributes.js#L349
      xanchor = 'left',
      font = font_for_labels,
      showarrow = FALSE
  ) %>%
    # Include a label showing what the 137.5% bar means
    add_annotations(
      x = 137.5,
      y = num_institutions - 1,
      text = '137.5% of designed capacity',
      xref = "x",
      yref = "y",
      showarrow = TRUE,
      arrowhead = 4,
      arrowsize = .5,
      ax = 20,
      ay = -40
  ) %>%
    layout(
      title = 'CA State Prison Population Overcrowding, Dec 2017',
      xaxis = list(title = "Percent Occupied"),
      yaxis = list(title = "",
                   zeroline = FALSE,
                   showline = FALSE,
                   showticklabels = FALSE,
                   showgrid = FALSE),
      barmode = 'group',
      # Include a vertical line showing the 137.5% threshold
      shapes = list(type=line, x0=137.5, y0=0, x1=137.5, y1=num_institutions)
    )
  if (!is.null(path_to_save) && overwrite) {
    api_create(p, filename = path_to_save)
  }
}

plotly_scatter <- function(df, path_to_save=NULL, overwrite=FALSE) {
  # Used to set axis limits, we want a square grid
  axes_limit <- max(df$total_population) * 1.1
  
  p <- plot_ly(
    data = df,
    x = ~designed_capacity,
    y = ~total_population,
    type = 'scatter',
    name = 'Actual Population',
    hoverinfo = 'text',
    text = ~paste(
      'Institution: ',
      institution_name,
      '<br>',
      'Capacity: ', designed_capacity, ', Actual: ', total_population,
      '<br>',
      percent_occupied,
      '% occupied',
      sep = ''
    )
  ) %>%
    # Disable hovering over the lines, it's just confusing - we only want in enabled for points
    add_trace(y = ~overcrowded_limit, mode = 'lines', name = '"Overcrowding" Threshold', line = list(color = 'red'), hoverinfo='none') %>%
    add_trace(y = ~designed_capacity, mode = 'lines', name = 'Population = Capacity', hoverinfo='none') %>%
    # Styling stuff
    layout(
      title = 'Prison Population vs. Capacities, CA Dec 2017',
      xaxis = list(title = "Capacity of Institution", range = c(0, axes_limit)),
      yaxis = list(title = "Actual Population in Institution", range = c(0, axes_limit))
    )
  if (!is.null(path_to_save) && overwrite) {
    api_create(p, filename = path_to_save)
  }
}

example_distributions <- function() {
  institution_name <- c('A', 'B', 'C', 'D', 'E')
  designed_capacity <- c(100, 100, 100, 100, 100)
  total_population <- c(120, 120, 120, 120, 120)
  
  balanced_example <- data.frame(institution_name, designed_capacity, total_population)
  print(paste("Aggregate crowding:", sum(balanced_example$total_population) / sum(balanced_example$designed_capacity)))
  
  total_population <- c(100, 100, 100, 100, 200)
  unbalanced_example <- data.frame(institution_name, designed_capacity, total_population)
  print(paste("Aggregate crowding:", sum(unbalanced_example$total_population) / sum(unbalanced_example$designed_capacity)))
}

calc_pct_in_overcrowded <- function(df) {
  end_of_year_pct_in_overcrowded <- df %>%
    filter(month == '12') %>%
    group_by(year) %>%
    summarise(
      # Total number of people
      population_across_all = sum(total_population),
      designed_cap_across_all = sum(designed_capacity),
      num_prisons_exceeding_limit = sum(ifelse(num_exceeding_limit > 0, 1, 0)),
      total_num_prisons = n(),
      # Number of people in a prison that is exceeding the 137.5% limit
      total_in_prison_exceeding_limit = sum(ifelse(num_exceeding_limit > 0, total_population, 0)),
      # Number of people greater than the 137.5% limit. E.g. if designed cap is 100, 137.5 is limit, and prison has
      # 150 people, then this stat would be 150 - 137.5 = 12.5. If there were 12.5 fewer people in this prison, then
      # it wouldn't be technically "overcrowded"
      total_excession = sum(ifelse(num_exceeding_limit > 0, num_exceeding_limit, 0)),
      pct_overpopulated = (total_excession / population_across_all) * 100,
      pct_of_population_in_an_overcrowded = (total_in_prison_exceeding_limit / population_across_all) * 100,
      aggregate_pct_of_capacity = population_across_all / designed_cap_across_all
    )
  
  return(end_of_year_pct_in_overcrowded)
}

plot_pct_in_overcrowded <- function(df, path_to_save=NULL, overwrite=FALSE) {
  p <- plot_ly(
    data = df %>% filter(year > 2000),
    x = ~year,
    y = ~pct_of_population_in_an_overcrowded,
    type = 'scatter',
    mode = 'lines',
    hoverinfo = 'text',
    text = ~paste(
      'End of ',
      year,
      '<br>',
      num_prisons_exceeding_limit, ' out of ', total_num_prisons, ' exceeded 137.5% desgined capacity',
      '<br>',
      # Thanks to https://stackoverflow.com/a/12135122
      format(round(pct_of_population_in_an_overcrowded, 2), nsmall = 2),
      '% of prison population lived in an overcrowded prison',
      sep = ''
    )
  ) %>%
    # Styling stuff
    layout(
      title = 'Percent of CA Prison Population Living in an Overcrowded Prison',
      xaxis = list(title = "Year"),
      yaxis = list(title = "% of people in prisons exceeding 137.5% threshold", range=c(0, 101))
    )
  if (!is.null(path_to_save) && overwrite) {
    api_create(p, filename = path_to_save)
  }
}

plot_pct_exceeding_overcrowding <- function(df, path_to_save=NULL, overwrite=FALSE) {
  p <- plot_ly(
    data = df %>% filter(year > 2000),
    x = ~year,
    y = ~pct_overpopulated,
    type = 'scatter',
    mode = 'lines',
    hoverinfo = 'text',
    text = ~paste(
      'End of ',
      year,
      '<br>',
      num_prisons_exceeding_limit, ' out of ', total_num_prisons, ' exceeded 137.5% desgined capacity',
      '<br>',
      # Thanks to https://stackoverflow.com/a/12135122
      format(round(pct_overpopulated, 2), nsmall = 2),
      '% of prison population is exceeding 137.5% limit',
      sep = ''
    )
  ) %>%
    # Styling stuff
    layout(
      title = 'Percent of Prison Population Exceeding 137.5%',
      xaxis = list(title = "Year"),
      yaxis = list(title = "% of people exceeding 137.5% limit", range = c(0, max(df$pct_overpopulated)))
    )
  if (!is.null(path_to_save) && overwrite) {
    api_create(p, filename = path_to_save)
  }
}

summary_stats <- function(df) {
  total_prisons <- nrow(df)
  above_137 <- df %>% filter(percent_occupied > 137.5)
  num_above_137 <- nrow(above_137)
  print(paste(num_above_137, ' out of ', total_prisons, ' were above 137.5% ', num_above_137 / total_prisons, '%', sep=''))
  
  total_in_overcrowded <- sum(above_137$total_population)
  total_in_all <- sum(df$total_population)
  print(paste(total_in_overcrowded, ' out of ', total_in_all, ' were in an overcrowded prison, or ', total_in_overcrowded / total_in_all, '%', sep=''))
}

prep_data <- function() {
  data <- read.csv('data/monthly_cdcr_population.csv')
  with_stats <- data %>%
    mutate(
      overcrowded_limit = 1.375 * designed_capacity,
      num_exceeding_design = total_population - designed_capacity,
      num_exceeding_limit = total_population - overcrowded_limit
    )
  
  return(with_stats)
}

data <- prep_data()
end_of_2017 <- data %>% filter(year == '2017') %>% filter(month == '12')

summary_stats(end_of_2017)
plotly_barchart_of_pcts(end_of_2017, 'overcrowding-barchart-pcts')
plotly_scatter(end_of_2017, 'overcrowding-scatter-end-of-2017')

overcrowding_stats <- calc_pct_in_overcrowded(data)
plot_pct_in_overcrowded(overcrowding_stats, 'overcrowding-pct-in-overcrowded')
plot_pct_exceeding_overcrowding(overcrowding_stats, 'overcrowding-pct-exceeding-limit')
