# Load necessary library
# library(readr)

# Read the data from a CSV file
data <- read.csv("Data/data/zipcodes/32025.csv")

# print(data)
# # Ensure num_cases is treated as numeric
data$num_cases <- as.numeric(data$num_cases)

# # Calculate the first derivative (daily new cases)
data$first_derivative <- c(NA, diff(data$num_cases))

# Convert the date column to Date type
data$date <- as.Date(data$date, format="%Y-%m-%d")  # Adjust the format string as necessary



data$date <- as.Date(data$date, format = "%Y-%m-%d")

# Remove rows with NA values

# Assuming the first derivative might also have NA values from diff calculation
data <- na.omit(data)  # This removes all rows where any NAs are present

# Filter rows where the first derivative is negative

negative_derivative_dates <- data[data$first_derivative < 0, ]


# Display dates, negative derivatives, and new cases
print(negative_derivative_dates[c("date", "first_derivative", "new_cases")])



par(mfrow=c(2,1))

# Open a plotting window
plot(data$date, data$num_cases, type = "l", col = "blue", lwd = 2,
     xlab = "Date", ylab = "Cumulative Cases", 
     main = "Cumulative Cases and Daily Changes")

# Create a new plot for the first derivative on the same graph but with a different y-axis
plot(data$date, data$first_derivative, type = "l", col = "red", lwd = 2, axes = TRUE, xlab = "", ylab = "")
