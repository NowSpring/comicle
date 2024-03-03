import axios from "axios";

// ログイン用のaxiosインスタンス
const loginClient = axios.create({
  baseURL: "http://0.0.0.0:8000/",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

// API用のaxiosインスタンス
const apiClient = axios.create({
  baseURL: "http://0.0.0.0:8000/api",
  headers: {
    "Content-Type": "application/json",
  },
});

// リクエストを送信する前に実行されるインターセプターを追加
apiClient.interceptors.request.use((config) => {
  const token = window.localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Token ${token}`; // トークンを動的に設定
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});


export default {
  submitLogin(logininfo) {
    return loginClient.post("api-token-auth/", logininfo);
  },
  getComicMaster() {
    return apiClient.get("comic/master");
  },
  getComicVersion(title_id) {
    return apiClient.get(`comic/version?title_id=${ title_id }`);
  },
  getComicEpisode(title_version_id) {
    return apiClient.get(`comic/episode?title_version_id=${ title_version_id }`);
  },
  // getReviewMaster() {
  //   return apiClient.get("review/master");
  // },
  // postTicket(data) {
  //   return apiClient.post("tickets/", data);
  // },
  // updateTicket(id, data) {
  //   return apiClient.patch(`tickets/${id}/`, data);
  // },
  // deleteTicket(id) {
  //   return apiClient.delete(`tickets/${id}`);
  // },
};
