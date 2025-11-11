import React from "react";
import Button from "./Button"; // 
import "../assets/css/style.css";

const Main = () => {
  return (
    <main className="app-main">
      <div className="container text-center">
        <h1 className="main-title mb-2">Stock Prediction Portal</h1>
        <p className="lead main-desc mb-3">
          This stock prediction application utilizes machine learning
          techniques, specifically employing Keras and LSTM models within the
          Django framework. It forecasts future stock prices by analyzing
          long-term and short-term moving averages — tools used by analysts to
          make data-driven investment decisions.
        </p>

        <Button label="Login" variant="primary" />
      </div>
    </main>
  );
};

export default Main;
