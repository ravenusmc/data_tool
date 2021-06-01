<template>
  <div>
    <GraphCard
      :typeOne="typeOne"
      :data="sentiment_graph_data"
      :options="chartOptionsOne"
    >
    </GraphCard>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GraphCard from "@/components/charts/GraphCard.vue";

export default {
  name: "SentimentGraph",
  components: {
    GraphCard,
  },
  data() {
    return {
      typeOne: "LineChart",
      chartOptionsOne: {
        title: "Sentiment by Sentence",
        legend: { position: "top" },
        colors: ["#BF0D3E"],
        height: 500,
        animation: {
          duration: 1000,
          easing: "linear",
        },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    };
  }, // End of Data
  computed: {
		...mapGetters("text", ["sentiment_graph_data"]),
  }, // End Computed properties
};
</script>