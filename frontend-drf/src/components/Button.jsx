import React from "react";
import PropTypes from "prop-types";

const Button = ({ label, variant = "primary", onClick, size = "md" }) => {
  // Base bootstrap class
  let baseClass = "btn fw-semibold rounded-3 ";
  let sizeClass = size === "sm" ? "btn-sm px-3 py-1" : "px-4 py-2";
  let variantClass = `btn-${variant}`;

  return (
    <button
      className={`${baseClass} ${variantClass} ${sizeClass}`}
      onClick={onClick}
    >
      {label}
    </button>
  );
};

// Optional prop type validation
Button.propTypes = {
  label: PropTypes.string.isRequired,
  variant: PropTypes.string,
  onClick: PropTypes.func,
  size: PropTypes.string,
};

export default Button;
