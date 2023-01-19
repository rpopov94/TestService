<template>
  <div>
    <div v-for="(question, id) in questions" :key="id" class="mx-0 mx-sm-auto">
      <div  class="card">
        <div class="card-header bg-primary bg-new">
          <h5 class="card-title mt-2" id="exampleModalLabel">{{question.title}}</h5>
        </div>
        <div class="modal-body">
          <form class="px-4" action="">
            <div class="form-check mb-2">
              <input class="form-check-input" type="checkbox" name="exampleForm" id="radio3Example1" value="A" v-model="answer"/>
              <label class="form-check-label" for="radio3Example1">
                {{question.q1}}
              </label>
            </div>
          </form>
        </div>
        <div class="modal-body">
          <form class="px-4" action="">
            <div class="form-check mb-2">
              <input class="form-check-input" type="checkbox" name="exampleForm" id="radio3Example1" value="B" v-model="answer"/>
              <label class="form-check-label" for="radio3Example1">
                {{question.q2}}
              </label>
            </div>
          </form>
        </div>
        <div class="modal-body">
          <form class="px-4" action="">
            <div class="form-check mb-2">
              <input class="form-check-input" type="checkbox" name="exampleForm" id="radio3Example1" value="C" v-model="answer" />
              <label class="form-check-label" for="radio3Example1">
                {{question.q3}}
              </label>
            </div>
          </form>
        </div>
        <div class="modal-body">
          <form class="px-4" action="">
            <div class="form-check mb-2">
              <input class="form-check-input" type="checkbox" name="exampleForm" id="radio3Example1" value="D" v-model="answer"/>
              <label class="form-check-label" for="radio3Example1">
                {{question.q4}}
              </label>
            </div>
          </form>
        </div>
      </div>
    </div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>Complete</b-col>
        <b-col><b-button class="modifybtn" to="#">Send</b-button></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  name: "QTest",
  props: ["questions"],
  data() {
    return {
      answer: [],
    }
  },
}
</script>

<style scoped>
.modifybtn{
  display: block;
  float: right;
  margin-top: 0.5em;
}
</style>
