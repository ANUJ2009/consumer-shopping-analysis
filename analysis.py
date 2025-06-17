import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    """Load and clean the dataset."""
    df = pd.read_csv(file_path)
    df = df.dropna()  # Drop missing values
    df['Gender'] = df['Gender'].astype('category')
    df['Category'] = df['Category'].astype('category')
    df['Location'] = df['Location'].astype('category')
    df['Age_bracket'] = pd.cut(df['Age'], bins=[0, 18, 30, 45, 60, 100], 
                               labels=['0-18', '19-30', '31-45', '46-60', '61+'])
    return df

def generate_insights(df):
    """Generate key insights from the dataset."""
    insights = {
        'avg_purchase': round(df['Purchase Amount (USD)'].mean(), 2),
        'top_category': df['Category'].mode()[0],
        'promo_usage': round((df['Promo Code Used'] == 'Yes').mean() * 100, 2)
    }
    return insights

def generate_plots(df, output_dir='static/plots'):
    """Generate and save visualizations."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Plot 1: Purchase Amount by Gender and Age Bracket
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Age_bracket', y='Purchase Amount (USD)', hue='Gender', data=df)
    plt.title('Purchase Amount by Gender and Age Bracket')
    plt.xlabel('Age Bracket')
    plt.ylabel('Purchase Amount (USD)')
    plt.legend(title='Gender')
    plt.savefig(os.path.join(output_dir, 'purchase_by_gender_age.png'))
    plt.close()
    
    # Plot 2: Top 5 Product Categories
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Category', data=df, order=df['Category'].value_counts().index[:5])
    plt.title('Top 5 Product Categories Purchased')
    plt.xlabel('Count')
    plt.ylabel('Category')
    plt.savefig(os.path.join(output_dir, 'top_categories.png'))
    plt.close()
    
    # Plot 3: Promo Code Usage by Location (Top 10)
    top_locations = df['Location'].value_counts().index[:10]
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Location', hue='Promo Code Used', data=df[df['Location'].isin(top_locations)])
    plt.title('Promo Code Usage by Location (Top 10 Locations)')
    plt.xlabel('Location')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Promo Code Used')
    plt.savefig(os.path.join(output_dir, 'promo_by_location.png'))
    plt.close()
    
    # Plot 4: Correlation Heatmap
    numerical_cols = ['Age', 'Purchase Amount (USD)', 'Previous Purchases']
    correlation_matrix = df[numerical_cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix of Numerical Variables')
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
    plt.close()

def analyze_data(file_path):
    """Main function to analyze data and return results."""
    df = load_data(file_path)
    insights = generate_insights(df)
    generate_plots(df)
    return insights