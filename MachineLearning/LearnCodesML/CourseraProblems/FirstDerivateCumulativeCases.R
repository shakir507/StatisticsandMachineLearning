# Load necessary library
# library(readr)

# Read the data from a CSV file
data <- read.csv("Data/data/zipcodes/32025.csv")

print(data)
# # Ensure num_cases is treated as numeric
data$num_cases <- as.numeric(data$num_cases)

# # Calculate the first derivative (daily new cases)
data$first_derivative <- c(NA, diff(data$num_cases))

# # Load ggplot2 for plotting
library(ggplot2)

# Plot the first derivative
# ggplot(data, aes(x = 1:nrow(data), y = first_derivative)) +
#   geom_line() + 
#   labs(title = "First Derivative of Cumulative Cases", x = "Day", y = "Change in Cases") +
#   theme_minimal()

plot(data$first_derivative, type = "l", col = "blue", lwd = 2, xlab = "Day", ylab = "Change in Cases",
     main = "First Derivative of Cumulative Cases")
# # # Load necessary library
# # library(readr)

# # # Read the data from a CSV file
# # data <- read_csv("data.csv")

# # # Ensure num_cases is treated as numeric
# data$num_cases <- as.numeric(data$num_cases)
