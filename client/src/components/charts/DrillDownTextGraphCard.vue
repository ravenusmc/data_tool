<template>
  <div>
    <GChart
      :type="typeOne"
      :data="data"
      :options="options"
      :events="chartEvents"
      ref="gChart"
    />
    <div :class="modalClasses" class="fade" id="reject" role="dialog">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title make-bold">Drilldown Information</h4>
            <button type="button" class="close" @click="toggle()">
              &times;
            </button>
          </div>
          <div class="modal-body">
            <h2>Sentence:</h2>
            <p>{{ this.sentence }}</p>
            <h2>Sentiment:</h2>
            <p>{{ this.sentiment }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "GraphCard",
  props: ["typeOne", "data", "options"],
  computed: {
    ...mapGetters("text", ["textFile"]),
  },
  data() {
    return {
      sentence: "",
      sentiment: 0,
      modalClasses: ["modal", "fade"],
      chartEvents: {
        select: () => {
          //console.log(this.data) // This will show you the data kept for reference
          const chart = this.$refs.gChart.chartObject;
          const selection = chart.getSelection()[0];
          let row = selection.row + 1;
          let index = this.data[row][0] - 1;
          this.sentence = this.textFile.sentence_and_sentiment_list[
            index
          ].sentence;
          this.sentiment = this.textFile.sentence_and_sentiment_list[
            index
          ].sentiment;
          this.toggle();
        },
      }, // End Chart Events
    };
  }, // End of data
  methods: {
    toggle() {
      // document.body.className += " modal-open";
      let modalClasses = this.modalClasses;

      if (modalClasses.indexOf("d-block") > -1) {
        modalClasses.pop();
        modalClasses.pop();

        //hide backdrop
        let backdrop = document.querySelector(".modal-backdrop");
        document.body.removeChild(backdrop);
      } else {
        modalClasses.push("d-block");
        modalClasses.push("show");

        //show backdrop
        let backdrop = document.createElement("div");
        backdrop.classList = "modal-backdrop fade show";
        document.body.appendChild(backdrop);
      }
    },
  }, // End of Methods
};
</script>
