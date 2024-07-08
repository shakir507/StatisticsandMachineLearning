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

plot(data$date[data$negative_derivative], data$first_derivative[data$negative_derivative], 
     col="red", pch=20, cex=3, xlab="Date", ylab="First Derivative", main="Test Negative Derivatives")
# Add an abline to see the zero line
par(mfrow=c(2, 1))  # Set up a 2x1 plot area

# Plot for Cumulative Cases with points where new cases are negative
plot(data$date, data$num_cases, type = "l", col = "blue", lwd = 2,
     xlab = "Date", ylab = "Cumulative Cases", 
     main = "Cumulative Cases Over Time")
points(data$date[data$negative_new_cases], data$num_cases[data$negative_new_cases], 
       col = "red", pch = 20, cex = 3)

# Plot for First Derivative with points where derivatives are negative
plot(data$date, data$first_derivative, type = "l", col = "blue", lwd = 2,
     xlab = "Date", ylab = "First Derivative",
     main = "Daily Changes in Cases")
points(data$date[data$negative_derivative], data$first_derivative[data$negative_derivative], 
       col = "red", pch = 20, cex = 3)  # pch 20 is a solid circle

# Reset par to default
par(mfrow=c(1, 1))  # Reset plotting parameters
