import apiClient from "./AxiosClient.js";

export default {
  searchTF(query) {
    return apiClient.post("/tf", {
      query: query,
    });
  },
  searchTFIDF(query) {
    return apiClient.post("/tf_idf", {
      query: query,
    });
  },
  searchBM25(query) {
    return apiClient.post("/bm25", {
      query: query,
    });
  },
  searchsongname(query) {
    return apiClient.post("/song_name", {
      query: query,
    });
  },
  searchArtist(query) {
    return apiClient.post("/artist_name", {
      query: query,
    });
  },
};
