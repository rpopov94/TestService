<template>
  <v-form>
    <v-card v-for="(question, id) in questions" :key="id" class="mb-4">
      <v-card-title class="text-h6">{{ question.title }}</v-card-title>
        <v-container>
          <v-checkbox :key="`1${id}`" :label="question.q1" :value="question.q1" v-model="checked"/>
          <v-checkbox :key="`2${id}`" :label="question.q2" :value="question.q2" v-model="checked"/>
          <v-checkbox :key="`3${id}`" :label="question.q3" :value="question.q3" v-model="checked"/>
          <v-checkbox :key="`4${id}`" :label="question.q4" :value="question.q4" v-model="checked"/>
        </v-container>
      </v-card>
    <v-btn @click="submitAnswers">Submit Answers</v-btn>
    {{percent}}
  </v-form>
</template>

<script>
export default {
  props: {
    id: Number,
    questions: []
  },
  data() {
    return {
      percent: 0,
      checked: [],
    }
  },
  methods: {
    arrayDifferencePercent(arr1, arr2) {
      const mergedArray = arr1.concat(arr2);
      const filteredArray = mergedArray.filter(item => !arr1.includes(item) || !arr2.includes(item));
      return (filteredArray.length / Math.max(arr1.length, arr2.length)) * 100;
    },
    submitAnswers(){
      const correct = this.$store.getters["answers/getAnswers"]
      const temp = correct.concat(this.checked)
      this.percent = Math.round(100 - this.arrayDifferencePercent(correct, temp))

    }
  },
  created() {
    this.$store.dispatch('answers/fetchAnswers',  this.$route.params.id)
  }
}

</script>
