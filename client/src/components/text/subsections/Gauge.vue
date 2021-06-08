<template>
  <div>
    <Guage
      :data="widthCalculation"
      :options="chartOptionsOne"
    >
    </Guage>
    <p class="speechRating-paragraph center">
      The text file has an overall rating of {{ this.speechRating }}
    </p>
    <p class="make-bold center">Rating System:</p>
    <ul>
      <li :class="{ active: firstLevel }">0-25: Very Negative</li>
      <li :class="{ active: secondLevel }">26-50: Negative</li>
      <li :class="{ active: thirdLevel }">51-75: Positive</li>
      <li :class="{ active: fourthLevel }">76-100: Very Positive</li>
    </ul>
  </div>
</template>

<script>
import Guage from "@/components/charts/Guage.vue";

export default {
  name: "Gauge",
  components: {
    Guage, 
  },
  props: ["percentage"],
  data() {
    return {
      firstLevel: false, 
      secondLevel: false, 
      thirdLevel: false, 
      fourthLevel: false, 
      speechRating: "",
      typeOne: "Gauge",
      chartOptionsOne: {
        greenFrom: 75, greenTo: 100,
        yellowFrom: 25, yellowTo: 75,
        redFrom: 0, redTo: 25,
        height: 400,
        minorTicks: 5
      },
    };
  },
  computed: {
    widthCalculation() {
      let correctedValue = Math.round((0.5 * this.percentage + 0.5) * 100);
      if (correctedValue >= 0 && correctedValue <= 25) {
        this.speechRating = "Very Negative";
        this.firstLevel = true;
      } else if (correctedValue > 25 && correctedValue <= 50) {
        this.speechRating = "Negative";
        this.secondLevel = true;
      } else if (correctedValue > 50 && correctedValue <= 75) {
        this.speechRating = "Positive";
        this.thirdLevel = true;
      } else {
        this.speechRating = "Very Positive";
        this.fourthLevel = true;
      }
      let guageValues = [
        ["Label", "Value"],
        ["Rating", correctedValue],
      ];
      return guageValues;
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
  /* margin-top: 50%; */
  top: 10px;
  position: relative;
}

.speechRating-paragraph {
  margin-top: 15px;
}

.active {
  font-weight: bold;
}

</style>  
