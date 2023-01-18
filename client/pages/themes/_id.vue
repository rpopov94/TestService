<template>
    <div class="container">
      <h1>{{data.name}}</h1>
      <div v-for="question in data.questions" class="mx-0 mx-sm-auto">
        <div  class="card">
          <div class="card-header bg-primary">
            <h5 class="card-title text-white mt-2" id="exampleModalLabel">{{question.title}}</h5>
          </div>
          <div class="modal-body">
            <form class="px-4" action="">
              <div class="form-check mb-2">
                <input class="form-check-input" type="radio" name="exampleForm" id="radio3Example1" />
                <label class="form-check-label" for="radio3Example1">
                  {{question.q1}}
                </label>
              </div>
            </form>
          </div>
          <div class="modal-body">
            <form class="px-4" action="">
              <div class="form-check mb-2">
                <input class="form-check-input" type="radio" name="exampleForm" id="radio3Example1" />
                <label class="form-check-label" for="radio3Example1">
                  {{question.q2}}
                </label>
              </div>
            </form>
          </div>
          <div class="modal-body">
            <form class="px-4" action="">
              <div class="form-check mb-2">
                <input class="form-check-input" type="radio" name="exampleForm" id="radio3Example1" />
                <label class="form-check-label" for="radio3Example1">
                  {{question.q3}}
                </label>
              </div>
            </form>
          </div>
          <div class="modal-body">
            <form class="px-4" action="">
              <div class="form-check mb-2">
                <input class="form-check-input" type="radio" name="exampleForm" id="radio3Example1" />
                <label class="form-check-label" for="radio3Example1">
                  {{question.q4}}
                </label>
              </div>
            </form>
          </div>

        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import QForm from "@/src/components/QForm";

export default {
  name: "_id",
  components: {QForm},
  middleware: ["auth"],
  async asyncData({params}) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/themes/${params.id}/`);
    return {
      data
    }
  }
}
</script>

<style scoped>



</style>
