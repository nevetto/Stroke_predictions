import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

// import Predict from "./pages/Predict";
 

// const apiUrl = "/choreo-apis/awbo/backend/rest-api-be2/v1.0";
// const cors = require('cors');
//   Predict.use(cors());
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});



api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;