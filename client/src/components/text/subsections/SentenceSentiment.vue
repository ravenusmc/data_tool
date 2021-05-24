<template>
  <div>
    <section>
      <h4 class="sentence-area"><span>Sentence:</span> {{ this.sentence }}</h4>
      <br />
      <h4><span>Sentence Sentiment:</span> {{ this.sentenceSentiment }}</h4>
      <h4><span>Change Sentence:</span></h4>
      <div>
        <svg
          @click="changeSentence('up')"
          width="3em"
          height="3em"
          viewBox="0 0 16 16"
          class="bi bi-arrow-up-circle-fill svgLeft arrow"
          :fill="colorAttr('')"
          @mouseover="mouseOver"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            class="test"
            fill-rule="evenodd"
            d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354
					7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5
					5.707V11.5z"
          />
        </svg>
        <svg
          @click="changeSentence('down')"
          width="3em"
          height="3em"
          viewBox="0 0 16 16"
          class="bi bi-arrow-down-circle-fill svgRight"
          fill="#007bff"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5
					4.5a.5.5 0 0 0-1
					0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0
					0-.708-.708L8.5 10.293V4.5z"
          />
        </svg>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "SentenceSentiment",
  props: {
    textFile: Object,
  },
  data() {
    return {
      value: this.initalValue,
      hover: false,
    };
  },
  computed: {
    ...mapGetters("text", [
      "initalValue",
      "sentence",
      "sentenceSentiment",
      "textLength",
    ]),
  },
  methods: {
    ...mapActions("text", ["changeSentenceAndSentiment"]),
    colorAttr: function (color) {
      let test = 'red';
      console.log(color)
      // var my_color = "#007bff";
      // console.log("TEST");
      return test;
    },
    mouseOver: function () {
      this.colorAttr('#FF9900');
    },
    changeSentence(direction) {
      let value = this.initalValue;
      if (direction === "up") {
        value += 1;
      } else if (direction === "down") {
        value -= 1;
      }
      if (value > this.textLength - 1) {
        alert("The end of the text has been reached!");
      } else if (value < 0) {
        alert("You cannot go back any further");
      } else {
        const payload = {
          value,
        };
        this.changeSentenceAndSentiment({ payload });
      }
    },
  },
};
</script>

<style scoped>
section {
  border: 2px solid blue;
  text-align: center;
  margin-top: 50px;
  min-height: 100px;
  overflow: hidden;
}

.sentence-area {
  border: 2px solid red;
}

span {
  font-weight: bold;
}

.arrow {
  margin: 0 15px 0 15px;
}
</style>