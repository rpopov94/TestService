<template>
  <div>
    <div v-for="(question, id) in questions" :key="id" class="mx-0 mx-sm-auto">
      <div  class="card">
        <div class="card-header bg-primary bg-new">
          <h5 class="card-title mt-2" id="exampleModalLabel">{{question.title}}</h5>
        </div>
        <div class="modal-body">
          <form class="px-4" action="">
            <div class="form-check mb-2" v-for="(answer, index) in question.answers" :key="index">
              <input class="form-check-input" type="checkbox" :id="'question-' + id + '-answer-' + index" :value="answer" v-model="selectedAnswers[id]"/>
              <label class="form-check-label" :for="'question-' + id + '-answer-' + index">
                {{answer}}
              </label>
            </div>
          </form>
        </div>
      </div>
    </div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>Complete</b-col>
        <b-col><b-button class="modifybtn" to="#" @click="sendAnswers">Send</b-button></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  params: ["questions"],
  name: "TestPage",
  data() {
    return {
      questions: [],
      selectedAnswers: []
    };
  },
  methods: {
    async fetchQuestions() {
      // Make API request to fetch questions and answers
      // Assign response data to the `questions` array
      // Initialize the `selectedAnswers` array with the same length as `questions`
    },
    sendAnswers() {
      // Filter the `selectedAnswers` array to get the selected answers for each question
      // Send the selected answers to the server
    }
  },
  async created() {
    await this.fetchQuestions();
  }
};
</script>
