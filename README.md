# Short Put Neural Network #
#### Contributors
* Will Cutchin
* Erik Klem
* Yash Gollapudi

### Description


This project aims to create a LSTM neural network that will take finacial information for a given underlying over a given time and provide a delta value that is suggested to short puts at. This neural network will be trained on historical data over a given time and aim to give the highest sensable delta value whilest minimizing chances of being in the money at expiration.

### Assuptions
* Strategy
  * Shorting put option
* Days To Expiration 
  * Closest monthly expiration to 45 days DTE
* Selling
  * Selling one put contract at every strike from the 50Δ to 20Δ

## 📋 Table of Contents
   * [Objectives](#-objectives)
   * [Tasks](#-task-table)
   * [Implementation](#-implementation)
     * Structure
       * Inputs
       * Outputs  
   * [Math Required](#-math-required)
     * Formulas
     * Weighting
   * [Technology Stack](#-technology-stack)
   * [Results](#-results)
   * [References](#-references)
   * [Licenses](#-licenses)

## 📌 Objectives
* Create a neural network to find a informed data value for short puts on a given underlying
  * Implement a LSTM Neural Network From Scratch
    * Clean and Gather Financial Data for Training
    * Determine Inputs and Outputs for The Neural Network
    * Train the Neural Network With Financial Data
  * Create Visualization of Results
  * Release the Neural Network to Handle Real Time Data


## 🗓 Task Table
| Task           | Time required | Assigned to   | Current Status | Finished | 
|----------------|---------------|---------------|----------------|-----------|
| LSTM Neural Net Theory| > 4 Days       | Will/Erik/Yash   | In Progress   |   <li> [ ] </li>  |
| LSTM Neural Net Implementation| > 1 Week        | Will/Erik/Yash   | TODO  | <li> [ ] </li>     |
| LSTM Neural Net Training| > 2 Days      | Will/Erik/Yash   | TODO   | <li> [ ] </li>  |
| LSTM Neural Net Real Time| > 1 Days      | Will/Erik/Yash   | TODO   | <li> [ ] </li>  |
| NN Collect Data   | > 3 Days      | Will/Yash   | In Progress    |    <li> [ ] </li>     |
| NN Prepare Data   | > 2 hours     | Will/Yash   |   TODO         |    <li> [ ] </li>     |
| NN Object Cache   | > 1 hours     | Will/Yash   |   TODO         |    <li> [ ] </li>     |
| Visualization - Data   |  > 2 Days    | Will   |   TODO      |    <li> [ ] </li> |
| Visualization - Visualization   | > 2 Days     | Will   |   TODO      |    <li> [ ] </li> |
| Visualization - Real Time Results   | > 2 Days     | Will   |   TODO      |    <li> [ ] </li> |


## 🛠 Implementation
### Structure
* #### Inputs
* #### Outputs

## ✏️ Math Required
### Financial Formulas  
* #### Delta
  * ##### Formula
  * ##### Function
* #### Implied Volitility
* #### Strike Price
### Weighting Formulas

## ⚙ Technology Stack

## 📊 Results

## 🔗 References

## 📃 Licenses

