<template>
  <v-form>
    <v-card v-for="(question, id) in questions" :key="id" class="mb-4">
      <v-card-title class="text-h6">{{ question.title }}</v-card-title>
        <v-container>
          <v-checkbox :key="`1${id}`" :label="question.q1" :value="question.q1" v-model="checkedq1" />
          <v-checkbox :key="`2${id}`" :label="question.q2" :value="question.q2" v-model="checkedq2" />
          <v-checkbox :key="`3${id}`" :label="question.q3" :value="question.q3" v-model="checkedq3" />
          <v-checkbox :key="`4${id}`" :label="question.q4" :value="question.q4" v-model="checkedq4" />
        </v-container>
      </v-card>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      checkedq1: [],
      checkedq2: [],
      checkedq3: [],
      checkedq4: []
    }
  },
  props: {
    questions: []
  }
}

</script>
