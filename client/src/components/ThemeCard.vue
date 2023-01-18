<template>
  <div>
    <b-card
      :title="name"
      img-src="https://picsum.photos/600/300/?image=25"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
    >
      <b-card-text>

      </b-card-text>

      <b-button :to="`/themes/${link}/`" variant="primary">Перейти к тесту</b-button>
    </b-card>

  </div>
</template>
<script>
export default {
  props: ["link", "name"]
};
</script>
