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
        hAxis: {
          title: "Sentence Number",
        },
        vAxis: {
          title: "Sentiment",
        },
        legend: { position: "top" },
        colors: ["#007bff"],
        height: 400,
        animation: {
          duration: 1000,
          easing: "linear",
        },
      },
    };
  }, // End of Data
  computed: {
    ...mapGetters("text", ["sentiment_graph_data"]),
  }, 
};
</script>