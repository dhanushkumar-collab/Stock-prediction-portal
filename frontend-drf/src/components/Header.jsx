import React from "react";
import Button from "./Button"; // 👈 import new Button component

const Header = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark subtle-navbar px-4">
      <div className="container-fluid">
        <a className="navbar-brand fw-semibold fs-5 subtle-title" href="#">
          Stock Prediction Portal
        </a>

        <div className="d-flex ms-auto">
          <Button label="Login" variant="primary" size="sm" />
          <Button label="Register" variant="success" size="sm" />
        </div>
      </div>
    </nav>
  );
};

export default Header;
