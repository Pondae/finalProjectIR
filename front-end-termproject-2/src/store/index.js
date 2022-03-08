import { reactive } from "vue";
export default reactive({
  flashMessage: "",
  patient: null,
  user: null,
  item: null,
  Keepdata: [],
  Deldata: [],
  currentUser: JSON.parse(localStorage.getItem("user")),
});
