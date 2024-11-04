import pandas as pd

def process_sales_data(file_path):
    # Read the dataset
    df = pd.read_csv(file_path)

    # Calculate total sales and total quantity
    df['Total Sales'] = df['Price'] * df['Quantity']
    total_sales = df['Total Sales'].sum()
    total_quantity = df['Quantity'].sum()
    
    # Calculate average price per product
    average_price = df['Price'].mean()

    # Generate summary
    summary = {
        "Total Sales": total_sales,
        "Total Quantity Sold": total_quantity,
        "Average Price per Product": average_price
    }

    return summary

# Example usage
if __name__ == "__main__":
    file_path = "sales_data.csv"  # Path to the CSV file
    result = process_sales_data(file_path)
    print("Sales Data Summary:")
    for key, value in result.items():
        print(f"{key}: {value:.2f}")
