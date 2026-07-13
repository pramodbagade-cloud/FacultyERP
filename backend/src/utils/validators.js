const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const validatePassword = (password) => {
  return password && password.length >= 8;
};

const validateRollNumber = (rollNumber) => {
  return rollNumber && rollNumber.length > 0;
};

const validateDate = (dateString) => {
  const date = new Date(dateString);
  return date instanceof Date && !isNaN(date);
};

module.exports = {
  validateEmail,
  validatePassword,
  validateRollNumber,
  validateDate
};
