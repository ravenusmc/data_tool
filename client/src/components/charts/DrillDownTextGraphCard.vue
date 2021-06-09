<template>
  <div>
    <GChart
      :type="typeOne"
      :data="data"
      :options="options"
      :events="chartEvents"
      ref="gChart"
    />
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
      // chartOptionsDrillDown: {
      //     title: 'Sentiment During World War 1',
      //     legend: { position: 'top' },
      // }, // End Chart One Options
      chartEvents: {
        select: () => {
          //console.log(this.data) // This will show you the data kept for reference
          const chart = this.$refs.gChart.chartObject;
          const selection = chart.getSelection()[0];
          // I need to add one to the row because the first row contains the
          // column headers.
          let row = selection.row + 1;
          // This pulls out the specific date from the element that the user
          // clicked on
          let index = this.data[row][0] - 1;
          const payload = {
            sentence: this.textFile.sentence_and_sentiment_list[index].sentence,
            sentiment: this.textFile.sentence_and_sentiment_list[index].sentiment
					};
          // this.fetchEVADrillDownData({ payload })
        },
      }, // End Chart Events
    };
  }, // End of data
};
</script>