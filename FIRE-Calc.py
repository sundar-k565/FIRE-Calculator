import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class FIRECalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("FIRE Calculator Suite - Top 1% Investment Banking Tool")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f5f7fa")
        
        # Set up the main notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.fire_frame = ttk.Frame(self.notebook)
        self.home_frame = ttk.Frame(self.notebook)
        self.wedding_frame = ttk.Frame(self.notebook)
        self.children_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.fire_frame, text="FIRE Calculator")
        self.notebook.add(self.home_frame, text="Home Purchase")
        self.notebook.add(self.wedding_frame, text="Wedding Goal")
        self.notebook.add(self.children_frame, text="Children's Goals")
        
        # Initialize all calculators
        self.setup_fire_calculator()
        self.setup_home_calculator()
        self.setup_wedding_calculator()
        self.setup_children_calculator()
        
        # Apply custom styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TNotebook.Tab', padding=[20, 10], font=('Segoe UI', 10, 'bold'))
        self.style.configure('TFrame', background='#f5f7fa')
        self.style.configure('TLabel', background='#f5f7fa', font=('Segoe UI', 10))
        self.style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'), foreground='#2c3e50')
        self.style.configure('Result.TLabel', font=('Segoe UI', 11, 'bold'), foreground='#27ae60')
        self.style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=6)
        self.style.map('TButton', background=[('active', '#3498db')], foreground=[('active', 'white')])
        
    def setup_fire_calculator(self):
        # Input frame
        input_frame = ttk.Frame(self.fire_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Results frame
        results_frame = ttk.Frame(self.fire_frame)
        results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(input_frame, text="FIRE Calculator", 
                               style='Header.TLabel', font=('Segoe UI', 16, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Input fields
        inputs = [
            ("Current Age:", "age", 30),
            ("Retirement Age:", "retirement_age", 60),
            ("Current Portfolio (₹):", "portfolio", 2500000),
            ("Monthly Investment (₹):", "monthly_investment", 30000),
            ("Annual Step-up (%):", "step_up", 10),
            ("Expected Annual Return (%):", "return_rate", 12),
            ("Inflation Rate (%):", "inflation", 7),
            ("Monthly Expenses (₹):", "expenses", 100000)
        ]
        
        self.fire_inputs = {}
        for label_text, var_name, default in inputs:
            frame = ttk.Frame(input_frame)
            frame.pack(fill=tk.X, pady=5)
            
            label = ttk.Label(frame, text=label_text, width=25, anchor='w')
            label.pack(side=tk.LEFT)
            
            var = tk.StringVar(value=str(default))
            entry = ttk.Entry(frame, textvariable=var, width=15)
            entry.pack(side=tk.RIGHT)
            self.fire_inputs[var_name] = var
        
        # Calculate button
        calc_button = ttk.Button(input_frame, text="Calculate FIRE", 
                                command=self.calculate_fire)
        calc_button.pack(pady=20)
        
        # Results display
        self.fire_results = {}
        result_labels = [
            ("FIRE Number (₹):", "fire_number"),
            ("Years to Retirement:", "years_to_retire"),
            ("Projected Portfolio (₹):", "projected_portfolio"),
            ("Monthly Withdrawal (₹):", "monthly_withdrawal")
        ]
        
        for label_text, var_name in result_labels:
            frame = ttk.Frame(results_frame)
            frame.pack(fill=tk.X, pady=8)
            
            label = ttk.Label(frame, text=label_text, width=25, anchor='w', 
                             font=('Segoe UI', 10, 'bold'))
            label.pack(side=tk.LEFT)
            
            result_label = ttk.Label(frame, text="₹0", style='Result.TLabel')
            result_label.pack(side=tk.RIGHT)
            self.fire_results[var_name] = result_label
        
        # Chart placeholder
        self.fire_chart_frame = ttk.Frame(results_frame)
        self.fire_chart_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
    def setup_home_calculator(self):
        # Input frame
        input_frame = ttk.Frame(self.home_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Results frame
        results_frame = ttk.Frame(self.home_frame)
        results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(input_frame, text="Home Purchase Calculator", 
                               style='Header.TLabel', font=('Segoe UI', 16, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Input fields
        inputs = [
            ("Current Age:", "home_age", 30),
            ("Purchase Age:", "purchase_age", 35),
            ("Current Home Value (₹):", "home_value", 10000000),
            ("Down Payment (%):", "down_payment", 20),
            ("Loan Tenure (years):", "loan_tenure", 20),
            ("Interest Rate (%):", "interest_rate", 8.5),
            ("Property Appreciation (%):", "appreciation", 6),
            ("Current Rent (₹):", "current_rent", 25000)
        ]
        
        self.home_inputs = {}
        for label_text, var_name, default in inputs:
            frame = ttk.Frame(input_frame)
            frame.pack(fill=tk.X, pady=5)
            
            label = ttk.Label(frame, text=label_text, width=25, anchor='w')
            label.pack(side=tk.LEFT)
            
            var = tk.StringVar(value=str(default))
            entry = ttk.Entry(frame, textvariable=var, width=15)
            entry.pack(side=tk.RIGHT)
            self.home_inputs[var_name] = var
        
        # Calculate button
        calc_button = ttk.Button(input_frame, text="Calculate Home Purchase", 
                                command=self.calculate_home)
        calc_button.pack(pady=20)
        
        # Results display
        self.home_results = {}
        result_labels = [
            ("Future Home Value (₹):", "future_value"),
            ("Down Payment Required (₹):", "down_payment_amount"),
            ("Loan Amount (₹):", "loan_amount"),
            ("EMI (₹):", "emi"),
            ("Total Interest (₹):", "total_interest"),
            ("Savings Required/Month (₹):", "savings_required")
        ]
        
        for label_text, var_name in result_labels:
            frame = ttk.Frame(results_frame)
            frame.pack(fill=tk.X, pady=8)
            
            label = ttk.Label(frame, text=label_text, width=25, anchor='w', 
                             font=('Segoe UI', 10, 'bold'))
            label.pack(side=tk.LEFT)
            
            result_label = ttk.Label(frame, text="₹0", style='Result.TLabel')
            result_label.pack(side=tk.RIGHT)
            self.home_results[var_name] = result_label
        
        # Chart placeholder
        self.home_chart_frame = ttk.Frame(results_frame)
        self.home_chart_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
    def setup_wedding_calculator(self):
        # Input frame
        input_frame = ttk.Frame(self.wedding_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Results frame
        results_frame = ttk.Frame(self.wedding_frame)
        results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(input_frame, text="Wedding Goal Calculator", 
                               style='Header.TLabel', font=('Segoe UI', 16, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Input fields
        inputs = [
            ("Current Age:", "wedding_age", 28),
            ("Wedding Age:", "wedding_target_age", 32),
            ("Current Wedding Cost (₹):", "wedding_cost", 2000000),
            ("Wedding Inflation (%):", "wedding_inflation", 8),
            ("Expected Return (%):", "wedding_return", 10),
            ("Current Savings (₹):", "wedding_savings", 500000)
        ]
        
        self.wedding_inputs = {}
        for label_text, var_name, default in inputs:
            frame = ttk.Frame(input_frame)
            frame.pack(fill=tk.X, pady=5)
            
            label = ttk.Label(frame, text=label_text, width=25, anchor='w')
            label.pack(side=tk.LEFT)
            
            var = tk.StringVar(value=str(default))
            entry = ttk.Entry(frame, textvariable=var, width=15)
            entry.pack(side=tk.RIGHT)
            self.wedding_inputs[var_name] = var
        
        # Calculate button
        calc_button = ttk.Button(input_frame, text="Calculate Wedding Goal", 
                                command=self.calculate_wedding)
        calc_button.pack(pady=20)
        
        # Results display
        self.wedding_results = {}
        result_labels = [
            ("Future Wedding Cost (₹):", "future_cost"),
            ("Savings Gap (₹):", "savings_gap"),
            ("Monthly Savings Required (₹):", "monthly_savings"),
            ("Total Savings at Wedding (₹):", "total_savings")
        ]
        
        for label_text, var_name in result_labels:
            frame = ttk.Frame(results_frame)
            frame.pack(fill=tk.X, pady=8)
            
            label = ttk.Label(frame, text=label_text, width=25, anchor='w', 
                             font=('Segoe UI', 10, 'bold'))
            label.pack(side=tk.LEFT)
            
            result_label = ttk.Label(frame, text="₹0", style='Result.TLabel')
            result_label.pack(side=tk.RIGHT)
            self.wedding_results[var_name] = result_label
        
        # Chart placeholder
        self.wedding_chart_frame = ttk.Frame(results_frame)
        self.wedding_chart_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
    def setup_children_calculator(self):
        # Input frame
        input_frame = ttk.Frame(self.children_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Results frame
        results_frame = ttk.Frame(self.children_frame)
        results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(input_frame, text="Children's Goals Calculator", 
                               style='Header.TLabel', font=('Segoe UI', 16, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Input fields
        inputs = [
            ("Number of Children:", "num_children", 2),
            ("Child's Current Age:", "child_age", 5),
            ("Education Start Age:", "edu_age", 18),
            ("Current Education Cost (₹):", "edu_cost", 2000000),
            ("Education Inflation (%):", "edu_inflation", 10),
            ("Wedding Age:", "wedding_age", 25),
            ("Current Wedding Cost (₹):", "child_wedding_cost", 1500000),
            ("Wedding Inflation (%):", "child_wedding_inflation", 8),
            ("Monthly Maintenance (₹):", "maintenance", 5000),
            ("Maintenance Inflation (%):", "maintenance_inflation", 7),
            ("Expected Return (%):", "children_return", 11),
            ("Current Savings (₹):", "children_savings", 1000000)
        ]
        
        self.children_inputs = {}
        for label_text, var_name, default in inputs:
            frame = ttk.Frame(input_frame)
            frame.pack(fill=tk.X, pady=5)
            
            label = ttk.Label(frame, text=label_text, width=25, anchor='w')
            label.pack(side=tk.LEFT)
            
            var = tk.StringVar(value=str(default))
            entry = ttk.Entry(frame, textvariable=var, width=15)
            entry.pack(side=tk.RIGHT)
            self.children_inputs[var_name] = var
        
        # Calculate button
        calc_button = ttk.Button(input_frame, text="Calculate Children's Goals", 
                                command=self.calculate_children)
        calc_button.pack(pady=20)
        
        # Results display
        self.children_results = {}
        result_labels = [
            ("Total Education Cost (₹):", "total_edu_cost"),
            ("Total Wedding Cost (₹):", "total_wedding_cost"),
            ("Total Maintenance Cost (₹):", "total_maintenance"),
            ("Total Goal Amount (₹):", "total_goal"),
            ("Savings Gap (₹):", "children_savings_gap"),
            ("Monthly Savings Required (₹):", "children_monthly_savings")
        ]
        
        for label_text, var_name in result_labels:
            frame = ttk.Frame(results_frame)
            frame.pack(fill=tk.X, pady=8)
            
            label = ttk.Label(frame, text=label_text, width=25, anchor='w', 
                             font=('Segoe UI', 10, 'bold'))
            label.pack(side=tk.LEFT)
            
            result_label = ttk.Label(frame, text="₹0", style='Result.TLabel')
            result_label.pack(side=tk.RIGHT)
            self.children_results[var_name] = result_label
        
        # Chart placeholder
        self.children_chart_frame = ttk.Frame(results_frame)
        self.children_chart_frame.pack(fill=tk.BOTH, expand=True, pady=20)
    
    def calculate_fire(self):
        try:
            # Get input values
            age = float(self.fire_inputs["age"].get())
            retirement_age = float(self.fire_inputs["retirement_age"].get())
            portfolio = float(self.fire_inputs["portfolio"].get())
            monthly_investment = float(self.fire_inputs["monthly_investment"].get())
            step_up = float(self.fire_inputs["step_up"].get()) / 100
            return_rate = float(self.fire_inputs["return_rate"].get()) / 100
            inflation = float(self.fire_inputs["inflation"].get()) / 100
            expenses = float(self.fire_inputs["expenses"].get())
            
            # Validate inputs
            if retirement_age <= age:
                messagebox.showerror("Error", "Retirement age must be greater than current age")
                return
                
            years_to_retire = retirement_age - age
            real_return = return_rate - inflation
            
            if real_return <= 0:
                messagebox.showerror("Error", "Real return (return - inflation) must be positive")
                return
                
            # Calculate FIRE number (using 4% rule adjusted for inflation)
            fire_number = expenses * 12 / real_return
            
            # Calculate projected portfolio
            total = portfolio
            monthly = monthly_investment
            
            for year in range(int(years_to_retire)):
                total = total * (1 + real_return) + monthly * 12
                monthly = monthly * (1 + step_up)
            
            # Calculate monthly withdrawal
            monthly_withdrawal = fire_number * real_return / 12
            
            # Update results
            self.fire_results["fire_number"].config(text=f"₹{fire_number:,.0f}")
            self.fire_results["years_to_retire"].config(text=f"{years_to_retire:.1f} years")
            self.fire_results["projected_portfolio"].config(text=f"₹{total:,.0f}")
            self.fire_results["monthly_withdrawal"].config(text=f"₹{monthly_withdrawal:,.0f}")
            
            # Create chart
            self.create_fire_chart(age, retirement_age, portfolio, monthly_investment, 
                                  step_up, real_return, fire_number)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def create_fire_chart(self, age, retirement_age, portfolio, monthly_investment, 
                         step_up, real_return, fire_number):
        # Clear previous chart
        for widget in self.fire_chart_frame.winfo_children():
            widget.destroy()
            
        # Create data for chart
        years = np.arange(age, retirement_age + 1)
        portfolio_values = []
        current_portfolio = portfolio
        current_monthly = monthly_investment
        
        for i, year in enumerate(years):
            if i == 0:
                portfolio_values.append(current_portfolio)
            else:
                current_portfolio = current_portfolio * (1 + real_return) + current_monthly * 12
                portfolio_values.append(current_portfolio)
                current_monthly = current_monthly * (1 + step_up)
        
        # Create the chart
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(years, portfolio_values, 'b-', linewidth=2.5, label='Portfolio Value')
        ax.axhline(y=fire_number, color='r', linestyle='--', label='FIRE Number')
        ax.set_xlabel('Age')
        ax.set_ylabel('Portfolio Value (₹)')
        ax.set_title('Portfolio Growth vs FIRE Number')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, self.fire_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def calculate_home(self):
        try:
            # Get input values
            current_age = float(self.home_inputs["home_age"].get())
            purchase_age = float(self.home_inputs["purchase_age"].get())
            home_value = float(self.home_inputs["home_value"].get())
            down_payment_pct = float(self.home_inputs["down_payment"].get()) / 100
            loan_tenure = float(self.home_inputs["loan_tenure"].get())
            interest_rate = float(self.home_inputs["interest_rate"].get()) / 100
            appreciation = float(self.home_inputs["appreciation"].get()) / 100
            current_rent = float(self.home_inputs["current_rent"].get())
            
            # Validate inputs
            if purchase_age <= current_age:
                messagebox.showerror("Error", "Purchase age must be greater than current age")
                return
                
            years_to_purchase = purchase_age - current_age
            
            # Calculate future home value
            future_value = home_value * ((1 + appreciation) ** years_to_purchase)
            
            # Calculate down payment and loan amount
            down_payment_amount = future_value * down_payment_pct
            loan_amount = future_value - down_payment_amount
            
            # Calculate EMI
            monthly_rate = interest_rate / 12
            months = loan_tenure * 12
            emi = loan_amount * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
            
            # Calculate total interest
            total_payment = emi * months
            total_interest = total_payment - loan_amount
            
            # Calculate savings required
            savings_required = down_payment_amount / (years_to_purchase * 12)
            
            # Update results
            self.home_results["future_value"].config(text=f"₹{future_value:,.0f}")
            self.home_results["down_payment_amount"].config(text=f"₹{down_payment_amount:,.0f}")
            self.home_results["loan_amount"].config(text=f"₹{loan_amount:,.0f}")
            self.home_results["emi"].config(text=f"₹{emi:,.0f}")
            self.home_results["total_interest"].config(text=f"₹{total_interest:,.0f}")
            self.home_results["savings_required"].config(text=f"₹{savings_required:,.0f}")
            
            # Create chart
            self.create_home_chart(current_age, purchase_age, home_value, future_value, 
                                  down_payment_amount, appreciation)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def create_home_chart(self, current_age, purchase_age, current_value, future_value, 
                         down_payment, appreciation):
        # Clear previous chart
        for widget in self.home_chart_frame.winfo_children():
            widget.destroy()
            
        # Create data for chart
        years = np.arange(current_age, purchase_age + 1)
        values = [current_value * ((1 + appreciation) ** (year - current_age)) for year in years]
        
        # Create the chart
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(years, values, 'g-', linewidth=2.5, label='Home Value')
        ax.axhline(y=down_payment, color='orange', linestyle='--', label='Down Payment Required')
        ax.set_xlabel('Age')
        ax.set_ylabel('Value (₹)')
        ax.set_title('Home Value Appreciation')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, self.home_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def calculate_wedding(self):
        try:
            # Get input values
            current_age = float(self.wedding_inputs["wedding_age"].get())
            wedding_age = float(self.wedding_inputs["wedding_target_age"].get())
            wedding_cost = float(self.wedding_inputs["wedding_cost"].get())
            inflation = float(self.wedding_inputs["wedding_inflation"].get()) / 100
            return_rate = float(self.wedding_inputs["wedding_return"].get()) / 100
            current_savings = float(self.wedding_inputs["wedding_savings"].get())
            
            # Validate inputs
            if wedding_age <= current_age:
                messagebox.showerror("Error", "Wedding age must be greater than current age")
                return
                
            years_to_wedding = wedding_age - current_age
            
            # Calculate future wedding cost
            future_cost = wedding_cost * ((1 + inflation) ** years_to_wedding)
            
            # Calculate savings gap
            savings_gap = future_cost - current_savings
            
            if savings_gap < 0:
                savings_gap = 0
                monthly_savings = 0
            else:
                # Calculate monthly savings required
                monthly_rate = return_rate / 12
                months = years_to_wedding * 12
                if monthly_rate == 0:
                    monthly_savings = savings_gap / months
                else:
                    monthly_savings = savings_gap * monthly_rate / ((1 + monthly_rate) ** months - 1)
            
            # Calculate total savings at wedding
            total_savings = current_savings * ((1 + return_rate) ** years_to_wedding) + \
                           monthly_savings * 12 * (((1 + return_rate) ** years_to_wedding - 1) / return_rate) if return_rate > 0 else \
                           current_savings + monthly_savings * 12 * years_to_wedding
            
            # Update results
            self.wedding_results["future_cost"].config(text=f"₹{future_cost:,.0f}")
            self.wedding_results["savings_gap"].config(text=f"₹{savings_gap:,.0f}")
            self.wedding_results["monthly_savings"].config(text=f"₹{monthly_savings:,.0f}")
            self.wedding_results["total_savings"].config(text=f"₹{total_savings:,.0f}")
            
            # Create chart
            self.create_wedding_chart(current_age, wedding_age, wedding_cost, future_cost, 
                                     current_savings, monthly_savings, return_rate)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def create_wedding_chart(self, current_age, wedding_age, current_cost, future_cost, 
                            current_savings, monthly_savings, return_rate):
        # Clear previous chart
        for widget in self.wedding_chart_frame.winfo_children():
            widget.destroy()
            
        # Create data for chart
        years = np.arange(current_age, wedding_age + 1)
        savings_values = []
        current_sav = current_savings
        
        for i, year in enumerate(years):
            if i == 0:
                savings_values.append(current_sav)
            else:
                current_sav = current_sav * (1 + return_rate) + monthly_savings * 12
                savings_values.append(current_sav)
        
        # Create the chart
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(years, savings_values, 'm-', linewidth=2.5, label='Savings')
        ax.axhline(y=future_cost, color='r', linestyle='--', label='Wedding Cost')
        ax.set_xlabel('Age')
        ax.set_ylabel('Amount (₹)')
        ax.set_title('Wedding Savings vs Goal')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, self.wedding_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def calculate_children(self):
        try:
            # Get input values
            num_children = int(self.children_inputs["num_children"].get())
            child_age = float(self.children_inputs["child_age"].get())
            edu_age = float(self.children_inputs["edu_age"].get())
            edu_cost = float(self.children_inputs["edu_cost"].get())
            edu_inflation = float(self.children_inputs["edu_inflation"].get()) / 100
            wedding_age = float(self.children_inputs["wedding_age"].get())
            wedding_cost = float(self.children_inputs["child_wedding_cost"].get())
            wedding_inflation = float(self.children_inputs["child_wedding_inflation"].get()) / 100
            maintenance = float(self.children_inputs["maintenance"].get())
            maintenance_inflation = float(self.children_inputs["maintenance_inflation"].get()) / 100
            return_rate = float(self.children_inputs["children_return"].get()) / 100
            current_savings = float(self.children_inputs["children_savings"].get())
            
            # Validate inputs
            if edu_age <= child_age or wedding_age <= child_age:
                messagebox.showerror("Error", "Education and wedding ages must be greater than child's current age")
                return
                
            years_to_edu = edu_age - child_age
            years_to_wedding = wedding_age - child_age
            
            # Calculate education cost per child
            future_edu_cost = edu_cost * ((1 + edu_inflation) ** years_to_edu)
            total_edu_cost = future_edu_cost * num_children
            
            # Calculate wedding cost per child
            future_wedding_cost = wedding_cost * ((1 + wedding_inflation) ** years_to_wedding)
            total_wedding_cost = future_wedding_cost * num_children
            
            # Calculate maintenance cost
            total_maintenance = 0
            current_maintenance = maintenance
            for year in range(int(years_to_wedding)):
                total_maintenance += current_maintenance * 12
                current_maintenance *= (1 + maintenance_inflation)
            total_maintenance *= num_children
            
            # Total goal amount
            total_goal = total_edu_cost + total_wedding_cost + total_maintenance
            
            # Calculate savings gap
            savings_gap = total_goal - current_savings
            if savings_gap < 0:
                savings_gap = 0
                monthly_savings = 0
            else:
                # Calculate monthly savings required
                monthly_rate = return_rate / 12
                months = years_to_wedding * 12
                if monthly_rate == 0:
                    monthly_savings = savings_gap / months
                else:
                    monthly_savings = savings_gap * monthly_rate / ((1 + monthly_rate) ** months - 1)
            
            # Update results
            self.children_results["total_edu_cost"].config(text=f"₹{total_edu_cost:,.0f}")
            self.children_results["total_wedding_cost"].config(text=f"₹{total_wedding_cost:,.0f}")
            self.children_results["total_maintenance"].config(text=f"₹{total_maintenance:,.0f}")
            self.children_results["total_goal"].config(text=f"₹{total_goal:,.0f}")
            self.children_results["children_savings_gap"].config(text=f"₹{savings_gap:,.0f}")
            self.children_results["children_monthly_savings"].config(text=f"₹{monthly_savings:,.0f}")
            
            # Create chart
            self.create_children_chart(child_age, edu_age, wedding_age, total_goal, 
                                      current_savings, monthly_savings, return_rate)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def create_children_chart(self, child_age, edu_age, wedding_age, total_goal, 
                             current_savings, monthly_savings, return_rate):
        # Clear previous chart
        for widget in self.children_chart_frame.winfo_children():
            widget.destroy()
            
        # Create data for chart
        years = np.arange(child_age, wedding_age + 1)
        savings_values = []
        current_sav = current_savings
        
        for i, year in enumerate(years):
            if i == 0:
                savings_values.append(current_sav)
            else:
                current_sav = current_sav * (1 + return_rate) + monthly_savings * 12
                savings_values.append(current_sav)
        
        # Create the chart
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(years, savings_values, 'c-', linewidth=2.5, label='Savings')
        ax.axhline(y=total_goal, color='r', linestyle='--', label='Total Goal')
        ax.set_xlabel('Child Age')
        ax.set_ylabel('Amount (₹)')
        ax.set_title('Children\'s Savings vs Goal')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, self.children_chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = FIRECalculator(root)
    root.mainloop()