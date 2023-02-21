<template>
  <v-form>
    <div v-for="(question, id) in questions" :key="id">
        <h3>{{question.title}}</h3><br>
        <input type="checkbox" id="jack" :value="question.q1" v-model="checkedq1">
        <label for="jack">{{question.q1}}</label>
        <br>
        <input type="checkbox" id="john" :value="question.q2" v-model="checkedq2">
        <label for="john">{{question.q2}}</label>
        <br>
        <input type="checkbox" id="mike" :value="question.q3" v-model="checkedq3">
        <label for="mike">{{question.q3}}</label>
        <br>
        <input type="checkbox" id="mike" :value="question.q4" v-model="checkedq4">
        <label for="mike">{{question.q4}}</label>
        <br>
<!--        <span>Отмеченные имена: {{ checkedq1 }}-{{ checkedq2 }}-{{ checkedq3}}-{{ checkedq4 }}</span>-->
<!--        <v-form />-->
    </div>
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
