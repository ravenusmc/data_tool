<template>
  <div>
    <GraphCard
      :typeOne="typeOne"
      :data="word_count_graph_data"
      :options="chartOptionsOne"
    >
    </GraphCard>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import GraphCard from "@/components/charts/GraphCard.vue";

export default {
  name: "WordCountGraph",
  components: {
    GraphCard,
  },
  data() {
    return {
      typeOne: "BarChart",
      chartOptionsOne: {
        title: "Word Count Graph",
        hAxis: {
          title: "Word Count",
        },
        vAxis: {
          title: "Word",
        },
        legend: { position: "top" },
        colors: ["#BF0D3E"],
        height: 400,
        animation: {
          duration: 1000,
          easing: "linear",
        },
      },
    };
  }, // End of Data
  computed: {
    ...mapGetters("text", ["word_count_graph_data"]),
  },
};
</script>