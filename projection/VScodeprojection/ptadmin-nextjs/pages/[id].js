import Layout from "../compontent/Layout";
import { useRouter } from "next/router";
import Users from "../compontent/Users";
import Powers from "../compontent/Powers";
import JobControl from "../compontent/JobControl";

export default function Home({}) {
  const router = useRouter();
  const { id } = router.query;
  return (
    <Layout>
      {(id == "Users" && <Users />) ||
        (id == "Powers" && <Powers />) ||
        (id == "JobControl" && <JobControl />)}
    </Layout>
  );
}
