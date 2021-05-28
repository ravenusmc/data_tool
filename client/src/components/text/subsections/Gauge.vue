<template>
  <div>
    <div class="container"></div>
    <div class="fill-container" :style="{ width: widthCalculation + '%' }">
      <span>{{ widthCalculation }}%</span>
    </div>
    <p class='speechRating-paragraph center'>The text file has an overall rating of {{ this.speechRating }}</p>
    <p class='make-bold center'>
      Rating System:
    </p>
      <ul>
        <li>0-25: Very Negative</li>
        <li>26-50: Negative</li>
        <li>51-75: Positive</li>
        <li>76-100: Very Positive</li>
      </ul>
  </div>
</template>

<script>
export default {
  name: "Guage",
  props: ["percentage"],
  data() {
    return {
      speechRating: "",
    };
  },
  computed: {
    widthCalculation() {
      let correctedValue = Math.round((0.5 * this.percentage + 0.5) * 100);

      if (correctedValue >= 0 && correctedValue <= 25) {
        this.speechRating = "Very Negative";
      } else if (correctedValue > 25 && correctedValue <= 50) {
        this.speechRating = "Negative";
      } else if (correctedValue > 50 && correctedValue <= 75) {
        this.speechRating = "Positive";
      } else {
        this.speechRating = "Very Positive";
      }

      return correctedValue;
    },
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  height: 100px;
  top: 0;
  overflow: hidden;
  background-color: #fd7e14;
}

.fill-container {
  z-index: 1;
  height: 100px;
  top: 0;
  background-color: #007bff;
  margin-top: -100px;
}

span {
  font-size: 50px;
  margin-left: 65%;
  margin-top: 50%;
}

.speechRating-paragraph {
  margin-top: 15px;
}

</style>  
